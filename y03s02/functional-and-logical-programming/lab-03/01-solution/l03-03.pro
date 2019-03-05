% Run the goal (find Bob's daughter) and trace the program (F10) till the end
% goal: father(bob, X), f(X)
trace
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

