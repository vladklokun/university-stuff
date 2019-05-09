% Functional and Logical Programming: Homework 01
%
% Task 07: build an expert system
%
% Solution for SWI Prolog written by Vlad Klokun. This implementation
% is (supposedly?) ISO-compatible.
%
% Usage:
% (">" indicates terminal prompt,
%  "?-" — SWI Prolog interactive prompt).
% > swipl
% ?- [task07].
% ?- run.
% ...
% ?- halt.
% (SWI Prolog exited)
%

% Include necessary definitions. Use `include/1` to stay ISO-compatible
:- include('list_ops.pl').
:- include('decision_maker.pl').

% Make the predicate `client/11` dynamic.
:- dynamic client/11.

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

% Run the prompt for picking a vehicle.
% Reads user input and queries the database for a fitting fact.
run :-
    writeln("Expert System 'Moto vehicle picker'."),
    writeln("Let's pick a vehicle"),
    writeln("What's your name?"),
    % Start asking a user for input
    read(ClName),
    writeln("Which type of a vehicle do you prefer?"),
    read(Type),
    writeln("What should its minimum Displacement be?"),
    read(Displ_min),
    writeln("What should its maximum Displacement be?"),
    read(Displ_max),
    writeln("What should its minimum RPM be?"),
    read(RPM_min),
    writeln("What should its maximum RPM be?"),
    read(RPM_max),
    writeln("What transmission type do you prefer?"),
    read(Trans_type),
    writeln("What color do you prefer?"),
    read(Color),
    writeln("What should its minimum Fuel Consumption be?"),
    read(Fuel_Cons_min),
    writeln("What should its maximum Fuel Consumption be?"),
    read(Fuel_Cons_max),
    writeln("What is the maximum price you are willing to pay?"),
    read(Price_max),
    % Add the record about the current user
    assertz(
        client(ClName,
             Type, Displ_min, Displ_max, RPM_min, RPM_max, Trans_type,
             Color, Fuel_Cons_min, Fuel_Cons_max, Price_max)
    ),
    % Find all fitting offers
    findall(
        MotoID,
        fits_client(MotoID, ClName),
        FittingVehicles
    ),
    writeln("Looks like these offers fit you:"),
    % Print the list of all vehicles that fit the criteria
    print_list(FittingVehicles),
    write("No more suitable vehicles."),
    % And remove the current client, since we don't need info about
    % them anymore
    retract(
        client(ClName,
             Type, Displ_min, Displ_max, RPM_min, RPM_max, Trans_type,
             Color, Fuel_Cons_min, Fuel_Cons_max, Price_max)
    ).
