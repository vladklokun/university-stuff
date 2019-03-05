% Run the goal (find Bob's children). Should fail: print nothing 
% goal: father(Z, X), father(Z, Y), X <> Y

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
	father(bob, X).

