-- Parallel and Distributed Computing
-- Lab 01: Semaphores
-- By Vlad Klokun of SP-425
-- Compiled with GNAT Community (20190517-83)
--
With Ada.Integer_Text_IO, Ada.Text_IO, Ada.Synchronous_Task_Control;
Use Ada.Integer_Text_IO, Ada.Text_IO, Ada.Synchronous_Task_Control;

procedure Lab01 is

	N: integer := 5; -- vector and matrix dimensions

	type Vector is
		array (Positive range <>) of integer;
	type Matrix is
		array (Positive range <>, Positive range <>) of integer;

	P: integer := 3; -- processor count
	H: integer := N/P; -- vector chunk size

	-- Global variables
	MA: Matrix(1 .. N, 1 .. N);
	MB: Matrix(1 .. N, 1 .. N);
	C : Vector(1 .. N);
	MZ: Matrix(1 .. N, 1 .. N);
	B : Vector(1 .. N);
	ME: Matrix(1 .. N, 1 .. N);
	-- Shared resources
	a, a2, a3: integer;

	-- Semaphores
	-- Comment format:
	-- <Destination Thread>: <Explanation>
	Scr    : Suspension_Object; -- Crit. region
	S1mzbme: Suspension_Object; -- T1: MZ, B, ME input
	S2mzbme: Suspension_Object; -- T2: MZ, B, ME input
	S2mb   : Suspension_Object; -- T2: MB input
	S3mb   : Suspension_Object; -- T3: MB input
	S1c    : Suspension_Object; -- T1: C input
	S3c    : Suspension_Object; -- T3: C input
	S1a2   : Suspension_Object; -- T1: a2 done
	S1a3   : Suspension_Object; -- T1: a3 done
	S2a    : Suspension_Object; -- T2: a done
	S3a    : Suspension_Object; -- T3: a done
	S1mah2 : Suspension_Object; -- T1: MA_H2 done
	S1mah3 : Suspension_Object; -- T1: MA_H3 Done

	procedure InitVector(
		A: out Vector;
		size: Integer;
		val: Integer)
	is
	begin
		for i in 1 .. size loop
			A(i) := val;
		end loop;
	end InitVector;

	procedure PrintVector(
		A: Vector;
		size: Integer)
	is
	begin
		for i in 1 .. size loop
			Put(A(i), 3);
		end loop;
	end PrintVector;

	function VectorMul(
		A: Vector;
		B: Vector;
		start: Integer;
		stop: Integer)
		return Integer
	is
		res: Integer;
	begin
		res := 0;
		for i in start .. stop loop
			res := res + A(i) * B(i);
		end loop;
		return res;
	end VectorMul;

	procedure InitMatrix
		(A: out Matrix;
		 m: Integer;
		 n: Integer;
		 val: Integer)
	is
	begin
		for i in 1 .. m loop
			for j in 1 .. n loop
				A(i, j) := val;
			end loop;
		end loop;
	end InitMatrix;

	procedure PrintMatrix(
		A: Matrix;
		m: Integer;
		n: Integer)
	is
	begin
		for i in 1 .. m loop
			for j in 1 .. n loop
				Put(A(i, j), 3);
			end loop;
			New_Line;
		end loop;
	end PrintMatrix;

	procedure MMMul(
		A: Matrix;
		B: Matrix;
		C: in out Matrix;
		m: Integer;
		n: Integer;
		p: Integer;
		start_i: Integer;
		start_j: Integer
		)
	is
	begin
		InitMatrix(C, N, N, 0);
		for i in start_i .. m loop
			for j in start_j .. p loop
				for k in 1 .. n loop
					C(i,j) := C(i,j) + A(i,k) * B(k,j);
				end loop;
			end loop;
		end loop;
	end MMMul;

	procedure MMAdd(
		A: Matrix;
		B: Matrix;
		C: in out Matrix;
		m: Integer;
		n: Integer;
		start_i: Integer;
		start_j: Integer
		)
	is
	begin
		for i in start_i .. m loop
			for j in start_j .. n loop
				C(i,j) := A(i,j) + B(i,j);
			end loop;
		end loop;
	end MMAdd;

	procedure SMMul(
		A: Integer;
		B: Matrix;
		C: in out Matrix;
		m: Integer;
		n: Integer;
		start_i: Integer;
		start_j: Integer
		)
	is
	begin
		InitMatrix(C, m, p, 0);
		for i in start_i .. m loop
			for j in start_j .. n loop
				C(i,j) := A * B(i,j);
				null;
			end loop;
		end loop;
	end SMMul;

	procedure Run_Tasks is task T1;

		task body T1
		is
			C1: Vector(1 .. N);
			MZ1: Matrix(1 .. N, 1 .. N);
			MT1: Matrix(1 .. N, 1 .. N);
			MT2: Matrix(1 .. N, 1 .. N);
		begin
			put_line("Process T1 started");

			-- Initialize variables but do not consider them ready
			InitVector(B, N, 0);
			InitVector(C, N, 0);
			InitMatrix(MA, N, N, 0);
			InitMatrix(MB, N, N, 3);
			InitMatrix(MZ, N, N, 0);
			InitMatrix(ME, N, N, 0);

			-- MB Initialized
			Set_True(S2mb);
			Set_True(S3mb);

			-- Wait and Copy C
			Suspend_Until_True(S1c);
			Suspend_Until_True(Scr);
			Set_False(Scr);
			C1 := C;
			Set_True(Scr);

			-- Wait for MZ, B, Me
			Suspend_Until_True(S1mzbme);

			-- Copy B and MZ
			Suspend_Until_True(Scr);
			Set_False(Scr);
			MZ1 := MZ;
			Set_True(Scr);

			-- Compute first value of A
			Suspend_Until_True(Scr);
			Set_False(Scr);
			a := VectorMul(C, B, 1, 2);
			Set_True(Scr);

			-- Wait for a_2 and a_3
			Suspend_Until_True(S1a2);
			Suspend_Until_True(S1a3);

			-- When all parts are ready, put a together
			Suspend_Until_True(Scr);
			Set_False(Scr);
			a := a + a2 + a3;
			Set_True(Scr);
			-- Signal other threads
			Set_True(S2a);
			Set_True(S3a);

			-- Compute MA_{H}
			-- MT1 = MB * MZ
			MMMul(
				A => MB,
				B => MZ1,
				C => MT1,
				m => 2,
				n => N,
				p => N,
				start_i => 1,
				start_j => 1
			);

			-- MT2 = a * ME
			SMMul(
				A => a,
				B => ME,
				C => MT2,
				m => 2,
				n => N,
				start_i => 1,
				start_j => 1
			);

			-- MA = MT1 + MT2 = MB * MZ + a * ME
			MMAdd(
				A => MT1,
				B => MT2,
				C => MA,
				m => 2,
				n => N,
				start_i => 1,
				start_j => 1
			);

			-- MA_{H_{1}} is done, wait for others
			Suspend_Until_True(S1mah2);
			Suspend_Until_True(S1mah3);

			-- When MA_{H_{i}}, where i \in {1, 2, 3} are done too,
			-- print A.
			PrintMatrix(MA, N, N);
			Put_Line("T1 Finished.");
		end T1;

		task T2;
		task body T2
		is
			-- Local copies
			ac2: Integer;
			MZ2: Matrix(1..N, 1..N);
			-- Temporary values for computing MA_H
			MT1: Matrix(1..N, 1..N);
			MT2: Matrix(1..N, 1..N);
		begin
			Put_Line("Task T2 started.");
			-- Input C
			InitVector(C, N, 1);
			-- Signal other tasks that C is ready
			Set_True(S1c);
			Set_True(S3c);

			Suspend_Until_True(S2mzbme);

			-- Copy MZ2 and compute a2 in one critical section
			Suspend_Until_True(Scr);
			Set_False(Scr);
			MZ2 := MZ;
			a2 := VectorMul(B, C, 3, 4);
			Set_True(Scr);
			-- Signal that a2 is ready
			Set_True(S1a2);

			-- Wait until a is ready
			Suspend_Until_True(S2a);

			-- Copy a into this thread. Critical region.
			Suspend_Until_True(Scr);
			Set_False(Scr);
			ac2 := a;
			Set_True(Scr);

			-- Wait until MB is ready
			Suspend_Until_True(S2mb);

			-- Compute MA_{H}
			-- MT1 = MB * MZ
			MMMul(
				A => MB,
				B => MZ2,
				C => MT1,
				m => 4,
				n => N,
				p => N,
				start_i => 3,
				start_j => 1
			);

			-- MT2 = a * ME
			SMMul(
				A => ac2,
				B => ME,
				C => MT2,
				m => 4,
				n => N,
				start_i => 3,
				start_j => 1
			);

			-- MA = MT1 + MT2 = MB * MZ + a * ME
			MMAdd(
				A => MT1,
				B => MT2,
				C => MA,
				m => 4,
				n => N,
				start_i => 3,
				start_j => 1
			);
			-- Signal that MA_{H_{2}} is ready
			Set_True(S1mah2);
		end T2;

		task T3;
		task body T3
		is
			C3: Vector(1..N);
			ac3: Integer;
			MT1: Matrix(1..N, 1..N);
			MT2: Matrix(1..N, 1..N);
		begin
			Put_Line("Task T3 started.");
			-- Input MZ, B, ME
			InitMatrix(MZ, N, N, 1);
			InitVector(B, N, 1);
			InitMatrix(ME, N, N, 1);
			-- Signal other tasks that MZ, B, ME are ready.
			Set_True(S1mzbme);
			Set_True(S2mzbme);

			-- Wait until C is ready
			Suspend_Until_True(S3c);

			-- Copy shared objects and compute a_3. Crit. region.
			Suspend_Until_True(Scr);
			Set_False(Scr);
			C3 := C;
			a3 := VectorMul(B, C, 5, 5);
			-- Signal that a_3 is ready
			Set_True(Scr);
			Set_True(S1a3);

			-- Wait until a is ready
			Suspend_Until_True(S3a);

			-- Copy a into this thread. Critical region.
			Suspend_Until_True(Scr);
			Set_False(Scr);
			ac3 := a;
			Set_True(Scr);

			-- Wait until MB is ready
			Suspend_Until_True(S3mb);
			-- Compute MA_{H}
			-- MT1 = MB * MZ
			MMMul(
				A => MB,
				B => MZ,
				C => MT1,
				m => 5,
				n => N,
				p => N,
				start_i => 5,
				start_j => 1
			);
			-- MT2 = a * ME
			SMMul(
				A => ac3,
				B => ME,
				C => MT2,
				m => 5,
				n => N,
				start_i => 5,
				start_j => 1
			);

			-- MA = MT1 + MT2 = MB * MZ + a * ME
			MMAdd(
				A => MT1,
				B => MT2,
				C => MA,
				m => 5,
				n => N,
				start_i => 5,
				start_j => 1
			);
			-- Signal that MA_{H_{3}} is ready
			Set_True(S1mah3);
		end T3;

	begin
		null;
	end Run_Tasks;

	begin
		put_line("Main procedure started");
		-- Allow access to shared resource
		Set_True(Scr);
		Run_Tasks;
end Lab01;
