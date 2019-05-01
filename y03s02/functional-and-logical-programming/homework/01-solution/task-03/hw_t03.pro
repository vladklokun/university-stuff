domains
	brand,type,fuel_type,name=symbol
	engine_capacity=real
	price,date,num,pop=integer
predicates
	moto(num,brand,type,date,engine_capacity,fuel_type,price,pop)
	customer(num,name,brand,date,engine_capacity,fuel_type,price)
	zapysiv(integer)
	zapysivv(integer)
	kolvon(integer,integer)
	kolvonn(integer,integer)
	maxbike(integer,integer)
	question1
	question2
	question3
	question4
	pokaznyk (num, integer)  %pokaznyk engine_capacity za yakim sortuutsa zapisi
	plc(integer, integer)   %vidpovidae na pytannya skilky v spisku tovariv z pokaznykom menshe vvedenogo chisla
	plcc(integer, integer, integer)  %predikat dlya pidrahunku plc()
	print_s (integer)   % Drukue zapis, yaka zaymae zadane mistse v uporiadkovanomu spisku
	print_ss (integer,integer)   %Slujboviy predikat dlya print_s: prohodit po spisku ta drukue kojnu zapis yaka zaimae vkazane mistse
	print_all_s(integer) %drukue vporiadkovani za znachennam engine_capacity  zapisi

clauses
	moto(1,honda,scooter,2000,150,benz,10000,0).
	moto(2,suzuki,bike,2010,650,benz,19000,3).
	moto(3,hyosung,bike,2014,250,benz,15200,5).
	moto(4,yamaha,scooter,2011,50,benz,7500,1).
	
	zapysiv(4).

	pokaznyk (Number, PEC) :- moto(Number, _, _, _, EC,_, _, _), PEC = EC. 
                         %PEC - pokaznyk engine_capacity za yakim sortuutsa zapisi
		
	
	plc(C,S) :- zapysiv(Z), plcc(Z,C,S).

	plcc(0, _, S) :- S=0, !.  

 	plcc(N, C, S) :- N1=N-1, plcc (N1, C, S1), pokaznyk (N, PEC), PEC < C, S = S1+1.   

 	plcc(N, C, S) :- N1=N-1, plcc (N1, C, S1), pokaznyk (N, PEC), PEC >= C, S = S1.
	
	print_s (Zhel_Mesto) :- Zhel_Mesto<1, !.
	print_s (Zhel_Mesto) :- zapysiv(Z), Zhel_Mesto>Z, !.
	print_s (Zhel_Mesto) :- print_ss(1, Zhel_Mesto).  

	print_ss (Nstroki, _) :- zapysiv(Z), Nstroki>Z, !.	
									

	print_ss (Nstroki, Zhel_Mesto) :- pokaznyk (Nstroki, PEC), plc(PEC , S), S = Zhel_Mesto-1, moto(Nstroki, Name, _, _, _, _, _,_) , write(Name, " ", PEC ), nl,  
			
	N1 = Nstroki+1, print_ss(N1, Zhel_Mesto). %vivedenna tovaru, if znaydeno menshe znachenna engine_capacity z yakim porivnuutsa inshi znachenna.Perehid do obrobki nastupnogo znachenna
							
	print_ss (Nstroki, Zhel_Mesto) :- pokaznyk (Nstroki, PEC), plc(PEC , S), S <> Zhel_Mesto-1,N1 = Nstroki+1, print_ss(N1, Zhel_Mesto). %if ne znaideno mensche znachenna, to perehid do obrobki nastupnogo znachenna  

	customer(1,sano,suzuki,2015,650,benz,11000).
	customer(2,vano,yamaha,2012,100,benz,10000).
	zapysivv(2).

	kolvon(0,0) :- !.
	kolvon(L,K_N) :- N1=L-1,kolvon(N1,K1_N1),moto(L,_,_,_,_,_,G,_),
                         customer(_,sano,_,_,_,_,G1),G<=G1,K_N=K1_N1+1.
	kolvon(L,K_N) :- N1=L-1,kolvon(N1,K1_N1),moto(L,_,_,_,_,_,G,_),
                         customer(_,sano,_,_,_,_,G1),G>G1,K_N=K1_N1.

	maxbike(0,0) :- !.
	maxbike(L,M_N) :- N1=L-1,maxbike(N1,M1_N1),
                         moto(L,_,_,_,_,_,_,Pop),Pop>M1_N1,M_N=Pop.
	maxbike(L,M_N) :- N1=L-1,maxbike(N1,M1_N1),moto(L,_,_,_,_,_,_,Pop),Pop<=M1_N1,M_N=M1_N1.


	question1 :- zapysiv(Z), maxbike(Z,Pop), moto(_,A,_,_,_,_,_,Pop),
                    write(A," is the most popular motocycle").

	
	print_all_s (NNN) :- zapysiv(Z), NNN>Z, !.
	print_all_s (NNN) :- print_s (NNN), NNN1 = NNN+1, print_all_s (NNN1).	

	question2 :- print_all_s(1). %vivesti vporiadkovani zapisi.
	
	
	kolvonn(0,0) :- !.
	kolvonn(L,K_N):-N1=L-1, kolvonn(N1,K1_N1),  
                       moto(L,_,_,_,X,_,_,_),X>=60,K_N=K1_N1+1.	 	 
	kolvonn(L,K_N):-N1=L-1, kolvonn(N1,K1_N1), 
                       moto(L,_,_,_,X,_,_,_),X<60,K_N=K1_N1.

	question3 :- zapysiv(Z),kolvon(Z,Kolvo),
                    write("Kolichestvo predlosheniy dlia Sano = ",Kolvo),nl.
	
	question4 :- zapysiv(Z),kolvonn(Z,Kolvo),
                    write("Kolichestvo = ",Kolvo),nl.