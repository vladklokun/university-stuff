domains
	name   = string
	age    = integer
	height = real
	sex    = char

predicates
	person(name, age, height, sex)
	
clauses
	person("Sallie", 48, 1.58, 'f').
	person("Andrea", 34, 1.59, 'f').
	person("Ronnie", 80, 1.74, 'm').
	person("Jim",    35, 1.88, 'm').
	person("Edna",   75, 1.52, 'f').
	person("Sharon", 51, 1.54, 'f').

% person(X, _, _, 'm')
% person(X, _, Height, Sex), Height > 1.50.
% person(X, Age, Height, Sex), Sex = 'f', Age < 20.
% person(X, Age, Height, Sex), Sex = 'f', Age > 50.
% person(X, Age, Height, Sex), Sex = 'm', Height > 1.80.

