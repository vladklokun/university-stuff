% Functional and Logical Programming: Homework 01
%
% Task 05: use dynamic databases (dyn. predicates in case of SWI Prolog)
%
% Solution for SWI Prolog written by Vlad Klokun. This implementation
% is (supposedly?) ISO-compatible.
%
% Usage:
% (">" indicates terminal prompt,
%  "?-" — SWI Prolog interactive prompt).
% > swipl
% ?- [task05].
% ?- task01(MostPopularType, Count). % (Count can be ommited with "_").
% ?- task02(Sorted).
% ?- task03(Client, OfferCount).
% ?- task04(Client).
% ?- halt.
% (SWI Prolog exited)
%

% Include necessary definitions. Use `include/1` to stay ISO-compatible
:- include('moto_store.pl').

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

run :-
    writeln("Hello! Options:"),
    writeln("1. (add_moto)      Add a moto vehicle."),
    writeln("2. (remove_moto)   Remove a moto vehicle."),
    writeln("3. (add_client)    Add a client."),
    writeln("4. (remove_client) Remove a client."),
    read(X),
    process(X).

% Process option 1: add a moto vehicle
process(1) :- process(add_moto).
process(add_moto) :-
    writeln("You are adding a moto vehicle."),
    writeln("Please enter its parameters followed by a period (\".\")"),
    writeln("The name of the vehicle: "), read(Name),
    writeln("Its type: "), read(Type),
    writeln("Its displacement: "), read(Displacement),
    writeln("Its max RPM: "), read(Max_RPM),
    writeln("Its transmission type (auto, manual): "), read(Trans_Type),
    writeln("Its color: "), read(Color),
    writeln("Its fuel consumption (L/km): "), read(Fuel_Cons),
    writeln("Its price: "), read(Price),
    writeln("You entered:"),
    write("Name: "), write(Name), nl,
    write("Type: "), write(Type), nl,
    write("Displacement: "), write(Displacement), nl,
    write("Max RPM: "), write(Max_RPM), nl,
    write("Transmission type: "), write(Trans_Type), nl,
    write("Color: "), write(Color), nl,
    write("Fuel consumption: "), write(Fuel_Cons), nl,
    write("Price: "), write(Price), nl,
    % Write given facts to a dynamic database
    writeln("Adding the vehicle to the database..."),
    assertz(
        moto(Name, Type, Displacement, Max_RPM, Trans_Type, Color,
             Fuel_Cons, Price)
    ),
    writeln("Added successfully.").

% Process option 2: remove a moto vehicle
process(2) :- process(remove_moto).
process(remove_moto) :-
    writeln("You are removing a moto vehicle."),
    writeln("Which vehicle do you  want to remove?"),
    read(MotoIDToRemove),
    retract(
        moto(MotoIDToRemove, _, _, _, _, _, _, _)
    ).

% Process option 'add_client'
process(3) :- process(add_client).
process(add_client) :-
    writeln("You are adding a client."),
    write("Please enter the info about them (name and vehicle preference)"),
    write("followed by a period (\".\")\n"),
    writeln("Client's Name:"), read(Name),
    writeln("Preferred vehicle type:"), read(PrefType),
    writeln("Minimum Displacement:"), read(Displ_min),
    writeln("Maximum Displacement:"), read(Displ_max),
    writeln("Minimum RPM:"), read(RPM_min),
    writeln("Maximum RPM:"), read(RPM_max),
    writeln("Preferred transmission type:"), read(Pref_Trans_Type),
    writeln("Preferred color:"), read(Pref_Color),
    writeln("Minimum Fuel Consumption:"), read(Fuel_Cons_min),
    writeln("Maximum Fuel Consumption:"), read(Fuel_Cons_max),
    writeln("Preferred price:"), read(Pref_Price),
    writeln("You entered:"),
    writeln("Client's Name:"), writeln(Name),
    writeln("Preferred vehicle type:"), writeln(PrefType),
    writeln("Minimum Displacement:"), writeln(Displ_min),
    writeln("Maximum Displacement:"), writeln(Displ_max),
    writeln("Minimum RPM:"), writeln(RPM_min),
    writeln("Maximum RPM:"), writeln(RPM_max),
    writeln("Preferred transmission type:"), writeln(Pref_Trans_Type),
    writeln("Preferred color:"), writeln(Pref_Color),
    writeln("Minimum Fuel Consumption:"), writeln(Fuel_Cons_min),
    writeln("Maximum Fuel Consumption:"), writeln(Fuel_Cons_max),
    writeln("Preferred price:"), writeln(Pref_Price),
    assertz(
        client(Name, PrefType, Displ_min, Displ_max, RPM_min, RPM_max,
               Pref_Trans_Type, Pref_Color, Fuel_Cons_min, Fuel_Cons_max,
               Pref_Price)
    ).

% Process option 'remove_client'
process(remove_client) :-
    writeln("You are removing a client."),
    writeln("Please enter a name of a client who you wish to remove:"),
    read(Name),
    write("Removing client "), write(Name), write("...\n"),
    retract(
        client(Name, _, _, _, _, _, _, _, _, _, _)
    ).

