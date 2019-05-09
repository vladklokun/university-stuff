% Functional and Logical Programming: Homework 01
%
% Solution for SWI Prolog written by Vlad Klokun.
%
% decision_maker.pl
% Makes a decision whether a given vehicle fits the client or not
fits_client(MotoID, C) :-
% True if vehicle with ID `MotoID` fits a client with name `C`
    % Get a client and their preferences
    client(C, Pref_type, Displ_min, Displ_max, RPM_min, RPM_max,
           Pref_trans_type, Pref_color, FuelCons_min, FuelCons_max,
           Price_max),
    % Get an instance of a moto vehicle
    moto(MotoID, Type, Displ, RPM, Trans_type, Color, FuelCons, Price),
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
