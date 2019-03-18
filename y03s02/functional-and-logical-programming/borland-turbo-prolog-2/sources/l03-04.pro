% Run the goal and trace the program (F10) till the end
% goal: father(Z, X), father(Z, Y), X <> Y
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

