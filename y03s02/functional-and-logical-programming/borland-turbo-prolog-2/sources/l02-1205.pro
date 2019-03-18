domains
	person, activity = symbol.
	days = real.
predicates
	likes(person, activity).
	sewing_experience(person, days).
	can_sew_a_dress(person).

goal
	can_sew_a_dress(X). % Rule evaluation

clauses
	likes(john, cars).
	likes(timmy, sewing).
	likes(eric, sewing).
	likes(sally, cycling).
	likes(eva, sewing).

	sewing_experience(timmy, 156).
	sewing_experience(eric, 32).
	sewing_experience(eva, 80).

	can_sew_a_dress(Person) :-
		likes(Person, sewing), 
		sewing_experience(Person, Days), 
		Days > 64.

