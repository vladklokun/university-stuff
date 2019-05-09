% Functional and Logical Programming: Homework 01
%
% Task 04: use lists to describe objects of the field
%
% Solution for SWI Prolog written by Vlad Klokun. This implementation
% is (supposedly?) ISO-compatible and uses lists to represent objects of
% the given field
%
% Usage:
% (">" indicates terminal prompt,
%  "?-" — SWI Prolog interactive prompt).
% > swipl
% ?- [task03_swipl].
% ?- task01(MostPopularType, Count). % (Count can be ommited with "_").
% ?- task02(Sorted).
% ?- task03(Client, OfferCount).
% ?- task04(Client).
% ?- halt.
% (SWI Prolog exited)
%

% Include necessary definitions. Use `include/1` to stay ISO-compatible
:- include('moto_store.pl').

% Store's offer:
% moto(
%   1. Name — must be unique.
%   2. Specifications List.
% )
%
% Specification List = [
%   1. Type — type of the vehicle.
%   2. Displacement — volume of the engine.
%   3. RPM — vehicle's rotations per minute.
%   4. Transmisison type.
%   5. Color.
%   6. Fuel Consumption — in L/100 km.
%   7. Price.
% ].
moto(honda01,
     [scooter, 700, 12000, auto, black, 6, 8000]).
moto(yamaha01,
     [scooter, 600, 12000, manual, black, 8, 9000]).
moto(ducati01,
     [scooter, 800, 12000, auto, white, 7, 10000]).
moto(ducati02,
     [scooter, 600, 10000, auto, white, 6, 9000]).
moto(suzuki01,
     [bike, 1500, 12000, auto, black, 10, 10000]).

% Client and their preferences:
% client(
%   1. Name — must be unique.
%   2. Preference_List — a list of preferences.
% )
%
% Preference_List = [
%   Type, Displacement_min, Displacement_max, RPM_min, RPM_max, tran_type,
%   color, fuel_cons_min, fuel_cons_max, price
% ]
client(jeff,
       [scooter, 400, 900, 6000, 13000, auto, black, 3, 7, 20000]).
client(john,
       [bike, 1000, 1700, 8000, 14000, manual, black, 5, 7, 15000]).
client(neal,
       [bike, 900, 1700, 8000, 14000, auto, black, 5, 12, 15000]).
client(kent,
       [scooter, 400, 900, 6000, 13000, auto, white, 3, 7, 20000]).
client(kirk,
       [atv, 400, 900, 6000, 13000, auto, black, 3, 7, 20000]).
client(mark,
       [scooter, 400, 900, 6000, 13000, auto, black, 3, 7, 20000]).

% Task 01: get the most popular Type preferred by clients
task01(MostPopularType, Count) :-
    get_most_popular_pref(MostPopularType, Count).

% Task 02: Sort moto vehicles by displacement
task02(Sorted) :-
    sort_moto_by_displacement(Sorted).

% Task 03: find how many offers there are for a given `Client`
task03(Client, OfferCount) :-
    client_offers(Client, OfferCount).

% Task 04: find the client for whom the store has the most offers
task04(Client) :-
    client_most_offers(Client).
