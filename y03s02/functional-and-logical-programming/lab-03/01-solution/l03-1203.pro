% Run the goal (find and print all Bob's children). 
% goal: find a father of two kids with different sexes.

% Trace is unneeded for this task
% trace
predicates
	father(symbol, symbol)
	m(symbol)
	f(symbol)
	% 	father_ss_c_f(symbol)
	% 	father_ss_c_m(symbol)
	% father_ss_c(symbol)

clauses
	father(tom, ann).
	father(tom, liz).
	father(bob, tom).
	father(bob, liz).
	m(tom).
	m(bob).
	f(ann).
	f(liz).

% father_ss_c_f(F) :-
% 		father(F, C1), father(F, C2), C1 <> C2, f(C1), f(C2).
% 
% 	father_ss_c_m(F) :-
% 		father(F, C1), father(F, C2), C1 <> C2, m(C1), m(C2).
% 
% 	father_ss_c(F) :-
% 		father_ss_c_f(F);father_ss_c_m(F).

goal
	% father_ss_c(X), write(X), nl, fail.
	father(F, C1), father(F, C2), C1 <> C2, f(C1), f(C2), write(F), nl, fail ;
	father(F, C1), father(F, C2), C1 <> C2, m(C1), m(C2), write(F), nl, fail. 

