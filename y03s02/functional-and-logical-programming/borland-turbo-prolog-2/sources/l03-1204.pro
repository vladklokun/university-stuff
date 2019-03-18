% Run the goal (find and print all Bob's children). 
% goal: find a father of two kids with different sexes.

% Trace is unneeded for this task
% trace
predicates
	father(symbol, symbol)
	m(symbol)
	f(symbol)

clauses
	father(tom, ann).
	father(tom, liz).
	father(bob, tom).
	father(bob, liz).
	m(tom).
	m(bob).
	f(ann).
	f(liz).

goal
father(Father1, Child), father(Father2, Child), Father1 <> Father2, write(Child), nl, fail.

