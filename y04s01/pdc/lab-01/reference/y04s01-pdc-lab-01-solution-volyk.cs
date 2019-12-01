using System;
using System.Threading;

namespace Lab1_Semaphore
{
    class Program
    {
        public static int N = 4;
        public static int[] D, W, D1, D2, A = new int[N];
        public static int[,] MA, MZ;
        public static int e, e1, e2;
        public static Semaphore S0 = new Semaphore(0, 1); // semaphore that controls input
        public static Semaphore S1 = new Semaphore(0, 1); //Semaphore that controls finishing calculating the result A
        public static Thread T1 = new Thread(T1Part), T2 = new Thread(T2Part);

        public static void T1Part()
        {
            Console.WriteLine("T1 Started");
            // INIT MA
            MA = new int[N, N];
            for (int i = 0; i < N; i++)
            {
                for (int j = 0; j < N; j++)
                {
                    MA[i, j] = 1;
                }
            }
            // INIT MZ

            MZ = new int[N, N];
            for (int i = 0; i < N; i++)
            {
                for (int j = 0; j < N; j++)
                {
                    MZ[i, j] = 1;
                }
            }
            // INIT D
            D = new int[N];
            for (int i = 0; i < D.Length; i++)
            {
                D[i] = 1;
            }
            // INIT W
            W = new int[N];
            for (int i = 0; i < W.Length; i++)
            {
                W[i] = 1;
            }

            //init e
            e = 1;
            Console.WriteLine("T1 END INPUT");
            S0.Release();

            //CALCULATING
            Console.WriteLine("T1 Calculate");
            //CRITICAL REGION BEGIN
            Thread.BeginCriticalRegion();
            e1 = e;
            D1 = (int[])D.Clone();
            Thread.EndCriticalRegion();
            //CRITICAL REGION END

            //CALCULATING A
            //-W1*e
            int[] mul_e_WH = new int[W.Length];
            for (int i = 0; i < W.Length / 2; i++)
            {
                mul_e_WH[i] = W[i] * -e1;
            }

            //MAH + MZH
            int[,] MA1 = new int[N, N];
            for (int i = 0; i < MA.GetLength(0) / 2; i++)
            {
                for (int j = 0; j < MA.GetLength(1); j++)
                {
                    MA1[i, j] = MA[i, j] + MZ[i, j];

                }
            }
            int[] res2 = MultiplicationV(MA1, D1);

            int[] res = AddVectors(res2, mul_e_WH);
            for (int i = 0; i < A.Length / 2; i++)
            {
                A[i] = res[i];
            }


            S1.WaitOne();
            Console.WriteLine("T1 FINISHED");
            //print A
            Console.WriteLine("RESULT:");
            for (int i = 0; i < A.Length; i++)
            {
                Console.WriteLine(A[i]);
            }
            Console.WriteLine("PROGRAM FINISHED");
            Console.WriteLine("---------------------------------------------");
        }

        public static void T2Part()
        {

            Console.WriteLine("T2 Started");

            S0.WaitOne();

            //CRITICAL REGION BEGIN
            Thread.BeginCriticalRegion();
            e2 = e;
            D2 = (int[])D.Clone();
            Thread.EndCriticalRegion();
            //CRITICAL REGION END
            //CALCULATING
            Console.WriteLine("T2 Calculate");

            //calc A2
            int[] mul_e_WH = new int[W.Length];
            for (int i = 0; i < W.Length / 2; i++)
            {
                mul_e_WH[i] = W[i] * -e2;
            }

            //MAH + MZH
            int[,] MA2 = new int[N, N];
            for (int i = MA.GetLength(0) / 2; i < MA.GetLength(0); i++)
            {
                for (int j = 0; j < MA.GetLength(1); j++)
                {
                    MA2[i, j] = MA[i, j] + MZ[i, j];

                }
            }
            int[] res2 = MultiplicationV(MA2, D2);

            int[] res = AddVectors(res2, mul_e_WH);
            for (int i = A.Length / 2; i < A.Length; i++)
            {
                A[i] = res[i];
            }

            Console.WriteLine("T2 FINISHED");
            S1.Release();


        }

        static int[] MultiplicationV(int[,] a, int[] b)
        {

            int[] r = new int[a.GetLength(0)];
            for (int i = 0; i < a.GetLength(0); i++)
            {
                for (int j = 0; j < b.Length; j++)
                {

                    r[i] += a[i, j] * b[j];
                }
            }
            return r;
        }

        static int[] AddVectors(int[] a, int[] b)
        {
            int[] res = new int[a.Length];
            for (int i = 0; i < a.Length; i++)
            {
                res[i] = a[i] + b[i];
            }
            return res;
        }



        static void Main(string[] args)
        {
            Console.WriteLine("PROGRAM STARTED");
            T1.Start();
            T2.Start();
            Console.ReadKey();

        }


    }
}