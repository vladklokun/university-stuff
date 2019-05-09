% Functional and Logical Programming: Homework 01
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

:- include('pseudographics.pl').

% Store facts about objects in a dynamic database.
:- dynamic
    moto/8,
    client/11.

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

run :-
    print_header_window,
    print_header_greeting,
    % writeln("\u2502 Hello! Options:"),
    writeln("\u2502 1 \u2502 task01        \u2502 Find the most popular vehicle type. \u2502"),
    writeln("\u2502 2 \u2502 task02        \u2502 Sort vehicles by displacement.      \u2502"),
    writeln("\u2502 3 \u2502 task03        \u2502 Count offers for a giveen client.   \u2502"),
    writeln("\u2502 4 \u2502 task04        \u2502 Find a client with the most offers. \u2502"),
    writeln("\u2502 5 \u2502 add_moto      \u2502 Add a moto vehicle.                 \u2502"),
    writeln("\u2502 6 \u2502 remove_moto   \u2502 Remove a moto vehicle.              \u2502"),
    writeln("\u2502 7 \u2502 add_client    \u2502 Add a client.                       \u2502"),
    writeln("\u2502 8 \u2502 remove_client \u2502 Remove a client.                    \u2502"),
    print_footer_greeting,
    write("\u2502 Select option (N or S): "),
    read(X),
    process(X).

% Task 01: get the most popular Type preferred by clients
process(1) :- process(task01).
process(task01):-
    get_most_popular_pref(MostPopularType, _),
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    writeln("\u2502 Task 01: Find the most popular vehicle type."),
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    write("\u2502 The most popular type: "),
    write(MostPopularType), nl,
    writeln("\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500").

% Task 02: Sort moto vehicles by displacement
process(2) :- process(task02).
process(task02):-
    sort_moto_by_displacement(Sorted),
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    writeln("\u2502 Task 02: Print vehicles sorted by Displacement."),
    writeln("\u2502 Format: Displacement-Vehicle"),
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    print_list(Sorted),
    writeln("\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500").

% Task 03: find how many offers there are for a given `Client`
process(3) :- process(task03).
process(task03):-
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    writeln("\u2502 Task 03: count suitable offers for a given client."),
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    write("\u2502 Client's Name     "),
    read(Client),
    client_offers(Client, OfferCount),
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    write("\u2502 There are "), write(OfferCount), write(" offers "),
    write("for '"), write(Client), write("'"), nl,
    writeln("\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500").

% Task 04: find the client for whom the store has the most offers
process(4) :- process(task04).
process(task04):-
    client_most_offers(Client),
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    writeln("\u2502 Task 04: find the client with the most offers."),
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    write("\u2502 The client with the most offers: "),
    write(Client), nl,
    writeln("\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500").

% Process option 1: add a moto vehicle
process(5) :- process(add_moto).
process(add_moto) :-
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    writeln("\u2502 You are adding a moto vehicle."),
    writeln("\u2502 Please enter its parameters followed by a period ('.')"),
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    write("\u2502 The name of the vehicle              "),
    read(Name),
    write("\u2502 Its type                             "),
    read(Type),
    write("\u2502 Its displacement                     "),
    read(Displacement),
    write("\u2502 Its max RPM                          "),
    read(Max_RPM),
    write("\u2502 Its transmission type (auto, manual) "),
    read(Trans_Type),
    write("\u2502 Its color                            "),
    read(Color),
    write("\u2502 Its fuel consumption (L/km)          "),
    read(Fuel_Cons),
    write("\u2502 Its price                            "),
    read(Price),
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    writeln("\u2502 You entered:"),
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    write("\u2502 Name:                                \u2502"),
    write(Name), nl,
    write("\u2502 Type:                                \u2502"),
    write(Type), nl,
    write("\u2502 Displacement:                        \u2502"),
    write(Displacement), nl,
    write("\u2502 Max RPM:                             \u2502"),
    write(Max_RPM), nl,
    write("\u2502 Transmission type:                   \u2502"),
    write(Trans_Type), nl,
    write("\u2502 Color:                               \u2502"),
    write(Color), nl,
    write("\u2502 Fuel consumption:                    \u2502"),
    write(Fuel_Cons), nl,
    write("\u2502 Price:                               \u2502"),
    write(Price), nl,
    % Write given facts to a dynamic database
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    writeln("\u2502 Adding the vehicle to the database..."),
    assertz(
        moto(Name, Type, Displacement, Max_RPM, Trans_Type, Color,
             Fuel_Cons, Price)
    ),
    writeln("\u2502 Added successfully."),
    writeln("\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500").

% Process option 2: remove a moto vehicle
process(6) :- process(remove_moto).
process(remove_moto) :-
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    writeln("\u2502 You are removing a vehicle."),
    writeln("\u2502 Please enter a value folowed by a period."),
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    write("\u2502 Name of a vehicle: "),
    read(MotoID),
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    write("\u2502 Removing vehicle "), write(MotoID), write("...\n"),
    retract(
        moto(MotoID, _, _, _, _, _, _, _)
    ),
    write("\u2502 Vehicle '"), write(MotoID),
    write("' removed successfully.\n"),
    writeln("\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500").

% Process option 'add_client'
process(7) :- process(add_client).
process(add_client) :-
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    writeln("\u2502 You are adding a client."),
    writeln("\u2502 Please enter the info about them (name and vehicle preference) "),
    writeln("\u2502 followed by a period ('.')"),
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    write("\u2502 Client's Name               "), read(Name),
    write("\u2502 Preferred vehicle type      "), read(PrefType),
    write("\u2502 Minimum Displacement        "), read(Displ_min),
    write("\u2502 Maximum Displacement        "), read(Displ_max),
    write("\u2502 Minimum RPM                 "), read(RPM_min),
    write("\u2502 Maximum RPM                 "), read(RPM_max),
    write("\u2502 Preferred transmission type "), read(Pref_Trans_Type),
    write("\u2502 Preferred color             "), read(Pref_Color),
    write("\u2502 Minimum Fuel Consumption    "), read(Fuel_Cons_min),
    write("\u2502 Maximum Fuel Consumption    "), read(Fuel_Cons_max),
    write("\u2502 Preferred price             "), read(Pref_Price),
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    write("\u2502 You entered\n"),
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    write("\u2502 Client's Name               \u2502 "), writeln(Name),
    write("\u2502 Preferred vehicle type      \u2502 "), writeln(PrefType),
    write("\u2502 Minimum Displacement        \u2502 "), writeln(Displ_min),
    write("\u2502 Maximum Displacement        \u2502 "), writeln(Displ_max),
    write("\u2502 Minimum RPM                 \u2502 "), writeln(RPM_min),
    write("\u2502 Maximum RPM                 \u2502 "), writeln(RPM_max),
    write("\u2502 Preferred transmission type \u2502 "), writeln(Pref_Trans_Type),
    write("\u2502 Preferred color             \u2502 "), writeln(Pref_Color),
    write("\u2502 Minimum Fuel Consumption    \u2502 "), writeln(Fuel_Cons_min),
    write("\u2502 Maximum Fuel Consumption    \u2502 "), writeln(Fuel_Cons_max),
    write("\u2502 Preferred price             \u2502 "), writeln(Pref_Price),
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    write("\u2502 Adding client '"), write(Name), write("' to the database...\n"),
    assertz(
        client(Name, PrefType, Displ_min, Displ_max, RPM_min, RPM_max,
               Pref_Trans_Type, Pref_Color, Fuel_Cons_min, Fuel_Cons_max,
               Pref_Price)
    ),
    write("\u2502 Client '"), write(Name), write("' has been added.\n"),
    writeln("\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500").

% Process option 'remove_client'
process(8) :- process(remove_client).
process(remove_client) :-
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    writeln("\u2502 You are removing a client."),
    writeln("\u2502 Please enter a value folowed by a period."),
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    write("\u2502 Name of a client "),
    read(Name),
    writeln("\u251c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524"),
    write("\u2502 Removing client "), write(Name), write("..."), nl,
    retract(
        client(Name, _, _, _, _, _, _, _, _, _, _)
    ),
    write("\u2502 Client '"), write(Name), write("' has been removed.\n"),
    writeln("\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500").

