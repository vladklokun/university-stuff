domains
	person, activity = symbol

predicates
	likes(symbol, symbol)
	
clauses
	likes(ellen, reading).
	likes(john, computers).
	likes(eric, swimming).
	likes(david, computers).
	likes(mary, X) if likes(john, X).
	likes(gina, X) if likes(eric, X).

