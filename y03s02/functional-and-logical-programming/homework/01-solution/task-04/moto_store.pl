% Functional and Logical Programming: Homework 01
%
% Solution for SWI Prolog written by Vlad Klokun

:- include('list_ops.pl').

% Task 1: find the most popular type of moto vehicle
% Checks if client `Client` wants type `Type`
wants_type(Client, Type) :-
    client(Client, [Type, _, _, _, _, _, _, _, _, _]).

% Counts how many clients want type `Type`
% True if `Type` is wanted `C` times
count_type_preferences(Type, C) :-
    % Find all solutions where someone wants a type Type and put them in
    % a list `Z`
    findall(_, wants_type(_, Type), Z),
    % Count the solutions from the length of list `Z`
    length(Z, C).

% Finds all the preferred types of moto vehicles
% True iff list `ResTypes` matches a sorted list of unique types
all_preferred_types(ResTypes) :-
    % Find every type `Type` in client preference facts (these types can be
    % repeating)
    findall(Type, client(_, [Type, _, _, _, _, _, _, _, _, _]), Types),
    % Sort the types, which removes duplicates and makes each type unique,
    % in ascending order
    sort(Types, ResTypes).

prefs_all_types(AllTypesCount) :-
    all_preferred_types(AllTypes),
    prefs_types(AllTypes, AllTypesCount).

% Counts preferences for a given list of types
prefs_types([], []).
% Preference count for an empty list is an empty list
% True iff [Type | TypesTail] has a preference count of
% [TypeCount-Type | PrefsTail]
prefs_types([Type|TypesTail], [TypeCount-Type|PrefsTail]) :-
    count_type_preferences(Type, TypeCount),
    prefs_types(TypesTail, PrefsTail).

% Sorts a list of pairs of form Count - Type by its key value (Count) in
% descending order
get_sorted_type_prefs(PrefsDesc) :-
    % Count how many times a particular type of a moto vehicle is wanted
    % and put the results in list L1
    % count_all_type_prefs([], L1),
    prefs_all_types(AllTypesPrefs),
    % Sort the preference pairs by their keys — count of how many times
    % they are wanted
    keysort(AllTypesPrefs, PrefsAsc),
    % Reverse the sort so the list is sorted in descending order
    % This allows to get the top item as a list's Head
    reverse(PrefsAsc, PrefsDesc).

% Gets the most popular preference — the head of a list. Assumes a sorted list
% True iff the most popular preference is `Type` with `Count` preferences
get_most_popular_pref(Type, Count) :-
    get_sorted_type_prefs([Count-Type | _]).

% Task 2: print moto vehicles sorted by their engine capacity

% Finds all pairs of vehicles Name with their corresponding Engine Capacity
% and puts them into a list L
get_moto_by_displacement(L) :-
    findall(
                Displacement-Name,
                moto(Name, [_, Displacement, _, _, _, _, _]),
                L
           ).

% Sorts a list of pairs of form Engine Capacity-Name by its key value —
% Displacement in ascending order
sort_moto_by_displacement(Sorted) :-
    get_moto_by_displacement(L),
    keysort(L, Sorted).

% Task 3: count how many offers fit a client Client's wishes

% True iff vehicle with ID `MotoID` fits a client with name `C`
fits_client(MotoID, C) :-
    % Get a client and their preferences
    client(C,
           [Pref_type, Displ_min, Displ_max, RPM_min, RPM_max,
           Pref_trans_type, Pref_color, FuelCons_min, FuelCons_max,
           Price_max]
    ),
    % Get an instance of a moto vehicle
    moto(MotoID, [Type, Displ, RPM, Trans_type, Color, FuelCons, Price]),
    % Check if parameters fit the preference criteria:
    % Vehicle Type
    Type = Pref_type,
    % Displacement
    Displ >= Displ_min, Displ =< Displ_max,
    % RPM
    RPM >= RPM_min, RPM =< RPM_max,
    % Transmission type
    Trans_type = Pref_trans_type,
    % Color
    Color = Pref_color,
    % Fuel Consumption
    FuelCons >= FuelCons_min, FuelCons =< FuelCons_max,
    % Price
    Price =< Price_max.

% Counts the amount of offers for a given `Client`
% True iff there are N offers for client `Client`
fits_n_offers(Client, N) :-
    findall(MotoID, fits_client(MotoID, Client), Tmp),
    length(Tmp, N).

% Used to find how many offers there are for each client
% True if there are `OfferCount` offers for client `Client`
client_offers(Client, OfferCount) :-
    client(Client, [_, _, _, _, _, _, _, _, _, _]),
    fits_n_offers(Client, OfferCount).

% Task 4: find the client for whom the store has the most offers
% Uses predicates from Task 3

% Finds how many offers `OfferCount` there are for every client `Client`
all_offers(RL) :-
    findall(OfferCount-Client, client_offers(Client, OfferCount), RL).

% True if there are the most offers for client `Client`
client_most_offers(Client) :-
    % Get all possible offers for every client
    all_offers(Offers),
    % Sort them in ascending order
    keysort(Offers, OffersAscending),
    % Reverse the list to get the descending order. Client with the most
    % offers is now at the Head. Get the Head of the list and split the
    % pair `OfferCount-Client` into just the `Client`, discard other values
    reverse(OffersAscending, [_-Client | _]).
