predicates
	mkwininput
	mkwinoutput(string, string, string, string, string)
	main

goal
	main.
	
clauses
	main :- 
		% mkwininput.
		mkwininput.
	mkwininput :-
		makewindow(1, 7, 7, "Input info.", 0, 0, 25, 40), nl,
		write("Surname: "),
		readln(Surname),
		write("Name: "),
		readln(Name),
		write("Middle name: "),
		readln(Middlename),
		write("Address: "),
		readln(Address),
		write("Tel.: "),
		% readln(Tel), nl.
		readln(Tel), nl,
		mkwinoutput(Surname, Name, Middlename, Address, Tel).
		% makewindow(2, 7, 7, "Output", 0, 33, 14, 32), nl,
		% write("Name: ", Name, "\nSurname: ", Surname), nl.

	mkwinoutput(Surname, Name, Middlename, Address, Tel) :-
		makewindow(2, 191, 191, "Output", 0, 40, 25, 40), nl,
		write(Surname, 
		      "\n", Name,
	              "\n", Middlename,
	              "\n", Address,
	              "\n", Tel), nl.

