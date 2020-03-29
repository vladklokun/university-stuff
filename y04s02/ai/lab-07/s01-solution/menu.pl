:- dynamic
    known/3.

menuask(A, V, _) :-
    % If an attribute == value, succeed and do not search for alternatives.
    known(yes, A, V),
    !.
menuask(A, V, _) :-
    % If A = V is False, fail.
    \+ known(yes, A, V),
    fail.
menuask(A, V, MenuList) :-
    % If a value for an attribute is NOT set, prompt for it.
    \+ known(_, A, _),
    write('What is the value for '), write(A), write('?'), nl,
    write(MenuList), nl,
    read(X),
    check_val(X, A, V, MenuList),
    asserta( known(yes, A, X) ),
    X == V.

check_val(X, _, _, MenuList) :-
    member(X, MenuList),
    !.
check_val(X, A, V, MenuList) :-
    write(X), write(' is not a legal value, try again.'), nl,
    menuask(A, V, MenuList).

top_goal(X) :-
    season(X).

solve :-
    retractall(known(_, _, _)),
    top_goal(X),
    write('The answer is '), write(X), nl.
solve :-
    write('No answer found.'), nl.
