% Run the goal (find and print all Bob's children). 
% goal: father(X, Y), father(X, Z), Y <> Z, write(Y, ' ', Z), nl, fail.

% Trace is unneeded for this task
% trace
predicates
	father(symbol, symbol)
	m(symbol)
	f(symbol)

clauses
	father(tom, ann).
	father(bob, tom).
	father(bob, liz).
	m(tom).
	m(bob).
	f(ann).
	f(liz).

goal
	% father(X, Y), f(Y), father(X, Z), Y <> Z, write(Y, ' ', Z), nl, fail.
	
	% The following line prints no solution. 
	father(X, Y), f(Y), father(X, Z), Y > Z, write(Y, ' ', Z), nl, fail.

