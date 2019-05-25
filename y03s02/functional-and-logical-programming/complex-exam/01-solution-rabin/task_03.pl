sort_list(X, Y) :-
    mergesort(X, Y).

% Merge sort implementation
mergesort([], []).
mergesort([L], [L]).
mergesort([H|T], Res) :-
    length(T, Len),
    Len > 0,
    split_in_half([H|T], Half1, Half2),
    mergesort(Half1, Res1),
    mergesort(Half2, Res2),
    merge(Res1, Res2, Res),
    % Cut to find a single solution
    !.

merge([], L, L).
merge(L, [], L).
% If X is less than Y, put it first in a resulting list
merge([X|Xs], [Y|Ys], [X|TR]) :-
    X @=< Y,
    merge(Xs, [Y|Ys], TR).
% If Y is less than X, put it first in a resulting list
merge([X|Xs], [Y|Ys], [Y|TR]) :-
    Y @=< X,
    merge([X|Xs], Ys, TR).

split_in_half(L, Half1, Half2) :-
    length(L, Len),
    HalfIdx is Len // 2,
    split_at(L, HalfIdx, Half1, Half2).

% Split a list `L` at index `Idx` into two halfs: `Half1` and `Half2`
split_at(L, Idx, Part1, Part2) :-
    % If the length of the first part is `Idx`...
    length(Part1, Idx),
    % ...and lists `Part1` and `Part2` together form a list `L`, we split the
    % lists properly
    append(Part1, Part2, L).

% Check if `X` is not contained in a list
not_in(_, []).
not_in(X, [Y|Ys]) :-
    X \= Y,
    not_in(X, Ys).

% Check if there are no duplicates in a list
no_duplicates([]).
no_duplicates([X|Xs]) :-
    not_in(X, Xs),
    no_duplicates(Xs).

% Check if B is neither a min nor a max element in a 3-element list
is_not_min_or_max(B, L) :-
    length(L, 3),
    no_duplicates(L),
    % Sort the list to find min and max element
    sort_list(L, [_, B, _ | []]),
    % Cut to find a singlle solution
    !.
