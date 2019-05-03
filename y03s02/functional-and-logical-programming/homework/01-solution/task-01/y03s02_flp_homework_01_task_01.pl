%
% Written for SWI Prolog
%
% Usage:
% 1. Run the SWI Prolog REPL:
% swipl
%
% 2. Load the knowledge base into the SWIPL interpreter (notice no extension):
% [y03s02_flp_homework_01_task_01].
%
% 3. Evaluate your goal.
%
man(illya).
man(igor).
man(kostia).
man(misha).
man(petya).

woman(valia).
woman(masha).
woman(vika).
woman(nastia).

% bring_into_the_world(X, Y).
% X is a parent of Y
bring_into_the_world(vika, nastia).
bring_into_the_world(igor, nastia).
bring_into_the_world(vika, illya).
bring_into_the_world(igor, illya).
bring_into_the_world(kostia, vika).
bring_into_the_world(valia, vika).
bring_into_the_world(kostia, masha).
bring_into_the_world(valia, masha).
bring_into_the_world(masha, misha).

bring_into_the_world(kostia, petya).
bring_into_the_world(valia, petya).

offspring(X, Y) :-
% Checks if X is a child of Y
	bring_into_the_world(Y, X), X \= Y.

son(X, Y) :-
% Checks if X is a son of Y
	offspring(X, Y), man(X), X \= Y.

daughter(X, Y) :-
% Checks if X is a daughter of Y
	offspring(X, Y), woman(X), X \= Y.

father(X, Y) :-
	offspring(Y, X), man(X), X \= Y.

mother(X, Y) :-
	offspring(Y, X), woman(X), X \= Y.

grandfather(X, Z) :-
	offspring(Y, X), offspring(Z, Y), man(X), X \= Y, Y \= Z.

grandmother(X, Z) :-
	offspring(Y, X), offspring(Z, Y), woman(X), X \= Y, Y \= Z.

brother(X, Y) :-
	offspring(X, Z), offspring(Y, Z), man(X), X \= Y, Y \= Z.

sister(X, Y) :-
	offspring(X, Z), offspring(Y, Z), woman(X), X \= Y, Y \= Z.

cousin(X, Y) :-
% Wrong! Matches full siblings.
% The reason is the predicate does not check whether parents
% of `X` and `Y` — persons `K` and `Z` respectively — are different people.
	% Find `Z` that is a parent of `X`
	offspring(X, Z),
	% Find `G` that is a grandparent of `X`
	offspring(Z, G),
	% Find `K` that is a child of `X`'s grandparent
	offspring(K, G),
	% Find `Y` that is an another grandchild of `X`'s grandparent
	offspring(Y, K),
	% `X` and `Y` must be different people. Makes sense.
	X \= Y,
	% Check if `X` is its own parent. Why?
	X \= K,
	% Check if `Z` is its own parent. ??
	Z \= G,
	% Check if `K` is its own parent. ??
	K \= G,
	% Check if `Y` is its own parent. ??
	Y \= K.

cousin2(X, Y) :-
% Correct implementation of `cousin/2`
	% Find `Z` that is a parent of `X`
	offspring(X, Z),
	% Find `G` that is a grandparent of `X`
	offspring(Z, G),
	% Find `K` that is a child of `X`'s grandparent
	offspring(K, G),
	% a child should be different from `X`'s parent
	K \= Z,
	% Find `Y` that is an another grandchild of `X`'s grandparent
	offspring(Y, K),
	X \= Y.

cousin_fixed(X, Y) :-
% Now this predicate works properly: it matches only cousins.
	bring_into_the_world(ParentX, X),
	bring_into_the_world(ParentY, Y),
	(
		sister(ParentX, ParentY)
	;
		brother(ParentX, ParentY)
	).

aunt(X, Y) :-
	offspring(Y, Z), sister(X, Z), X \= Y, Y \= Z.

uncle(X, Y) :-
	offspring(Y, Z), brother(X, Z), X \= Y, Y \= Z.

