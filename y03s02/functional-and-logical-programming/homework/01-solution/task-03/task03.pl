% Functional and Logical Programming: Homework 01
%
% Task 03: "Moto Vehicles Store"
% T 03.01: find the most popular vehicle type
% T 03.02: sort vehicles by their displacement
% T 03.03: count suitable offers for a given client
% T 03.04: find the client for whom the store has the most offers
%
% Solution for SWI Prolog written by Vlad Klokun. This implementation
% is (supposedly?) ISO-compatible.
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
%   1. Name — must be unique;
%   2. Type — type of the vehicle;
%   3. Displacement — volume of the engine;
%   4. RPM — vehicle's rotations per minute;
%   5. Transmisison type;
%   6. Color;
%   7. Fuel Consumption — in L/100 km;
%   8. Price.
% ).
moto(honda01, scooter, 700, 12000, auto, black, 6, 8000).
moto(yamaha01, scooter, 600, 12000, manual, black, 8, 9000).
moto(ducati01, scooter, 800, 12000, auto, white, 7, 10000).
moto(ducati02, scooter, 600, 10000, auto, white, 6, 9000).
moto(suzuki01, bike, 1500, 12000, auto, black, 10, 10000).

% Client and their preferences:
% client(
%   Name — must be unique,
%   Type, EC_min, EC_max, RPM_min, RPM_max, tran_type, color,
%   fuel_cons_min, fuel_cons_max, price
% )
client(jeff, scooter, 400, 900, 6000, 13000, auto, black, 3, 7, 20000).
client(john, bike, 1000, 1700, 8000, 14000, manual, black, 5, 7, 15000).
client(neal, bike, 900, 1700, 8000, 14000, auto, black, 5, 12, 15000).
client(kent, scooter, 400, 900, 6000, 13000, auto, white, 3, 7, 20000).
client(kirk, atv, 400, 900, 6000, 13000, auto, black, 3, 7, 20000).
client(mark, scooter, 400, 900, 6000, 13000, auto, black, 3, 7, 20000).

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
