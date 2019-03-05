% Run the goal (find all the Bob's children) 
% goal: father(bob, X), write(X). 

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
	father(bob, X), write(X).

