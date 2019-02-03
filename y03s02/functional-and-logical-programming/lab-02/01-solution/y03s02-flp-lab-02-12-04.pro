domains
	person, activity = symbol.
predicates
	man(symbol).
	woman(symbol).
	likes(person, activity).

goal
	man(X), likes(X, sewing). % Compound goal with a variable

clauses
	man(john).
	man(timmy).
	man(eric).
	woman(sally).
	woman(eva).

	likes(john, cars).
	likes(timmy, sewing).
	likes(eric, sewing).
	likes(sally, cycling).
	likes(eva, sewing).

