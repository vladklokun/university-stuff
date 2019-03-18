domains
	beverage = symbol
	person   = symbol

predicates
	beverage(symbol)
	is_alcoholic(beverage)
	drank(person, beverage)
	is_drunk(person)
	is_not_drunk(person)

clauses
	beverage(water).
	beverage(soda).
	beverage(vodka).
	beverage(beer).

	is_alcoholic(vodka).
	is_alcoholic(beer).

	drank(tom, water).
	drank(sally, soda).
	drank(sally, vodka).
	drank(sally, soda).
	drank(peter, beer).

	is_drunk(X) if drank(X, Beverage), is_alcoholic(Beverage).
	is_not_drunk(X) if drank(X, Beverage), not(is_alcoholic(Beverage)).

