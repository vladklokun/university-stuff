% Functional and Logical Programming: Homework 01
%
% Solution for SWI Prolog written by Vlad Klokun
% List processing predicates to stay ISO-compatible.

print_list([]).
print_list([H|T]) :-
    write("VehicleID: "), writeln(H),
    print_list(T).
