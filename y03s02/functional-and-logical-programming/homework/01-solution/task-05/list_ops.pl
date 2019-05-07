% Functional and Logical Programming: Homework 01
%
% Solution for SWI Prolog written by Vlad Klokun
% List processing predicates to stay ISO-compatible.
% These override the default `reverse/2` predicate

% Predicate to wrap reversing
reverse(L, Reversed) :-
    % Used for initialization. Reverse using an empty accumulator
    reverse_acc(L, [], Reversed).

% Reverse a list using an accumulator
reverse_acc([H|T], Acc, Reversed) :-
    reverse_acc(T, [H|Acc], Reversed).
reverse_acc([], Acc, Acc).
