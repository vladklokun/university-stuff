% Solution for SWI Prolog
% moto(
%	1. Name --- must be unique;
%	2. Type,
%	3. Displacement --- volume of the engine;
%	4. RPM_max,
%	5. Transmisison type;
%	6. Color,
%	7. Fuel Consumption --- in L/100 km.
%	8. Price
% ).
moto(honda, scooter, 700, 12000, auto, black, 6, 10000).
moto(yamaha, scooter, 600, 12000, manual, black, 8, 10000).
moto(ducati, scooter, 800, 12000, auto, white, 7, 10000).
moto(suzuki, bike, 1500, 12000, auto, black, 10, 10000).

% client(
% 	Name, Type, EC_min, EC_max, RPM_min, RPM_max, tran_type, color,
% 	fuel_cons_min, fuel_cons_max, price
% )
client(jeff, scooter, 400, 900, 6000, 13000, auto, black, 3, 7, 20000).
client(john, bike, 20, 60, 6000, 12000, auto, black, 3, 7, 6000).
client(kent, scooter, 20, 60, 6000, 12000, auto, black, 3, 7, 6000).
client(kirk, atv, 20, 60, 6000, 12000, auto, black, 3, 7, 6000).
client(mark, bike, 20, 60, 6000, 12000, auto, black, 3, 7, 6000).

wants_type(Client, Type) :-
% Checks if client Client wants type Type
	client(Client, Type, _, _, _, _, _, _, _, _, _).

count_type_preferences(Type, C) :-
% Counts how many clients want type Type
% When Type is wanted C times
	% Find all solutions where someone wants a type Type
	findall(_, wants_type(_, Type), Z),
	% An count them
	length(Z, C).

append_scooter_count(L, L2) :-
	count_type_preferences(scooter, C),
	append(L, [C-scooter], L2).

append_bike_count(L, L2) :-
	count_type_preferences(bike, C),
	append(L, [C-bike], L2).

append_atv_count(L, L2) :-
	count_type_preferences(atv, C),
	append(L, [C-atv], L2).

count_all_type_prefs(L, RL) :-
	append_scooter_count(L, L1),
	append_bike_count(L1, L2),
	append_atv_count(L2, RL).

get_sorted_type_prefs(L, RL) :-
% Sorts a list of pairs of form Count - Type by its key value (Count) in
% descending order
	% Count how many times a particular type of a moto vehicle is wanted
	% and put the results in list L1
	count_all_type_prefs(L, L1),
	% Sort the preference pairs by their keys --- count of how many times
	% they are wanted
	keysort(L1, L2),
	% Reverse the sort so the list is sorted in descending order
	% This allows to get the top item as a list's Head
	reverse(L2, RL).

get_most_popular_pref(H) :-
	get_sorted_type_prefs([], [H | _]).
% Gets the top item in list --- its head. Assumes a sorted list

% Task 2: print moto vehicles sorted by their engine capacity
get_moto_ec(L) :-
% Finds all pairs of vehicles Name with their corresponding Engine Capacity
% and puts them into a list L
	findall(EC-Name, moto(Name, _, EC, _, _, _, _, _), L).

sort_moto_by_ec(RL) :-
% Sorts a list of pairs of form Engine Capacity - Name by its key value ---
% Engine Capacity in ascending order
	get_moto_ec(L),
	keysort(L, RL).

% Task 3: count how many offers fit a client Client's wishes
% TODO
fits_client(MotoID, C) :-
% True if vehicle with ID `MotoID` fits a client with name `C`
	client(C, Pref_type, Displ_min, Displ_max, RPM_min, RPM_max,
	       Pref_trans_type, Pref_color, FuelCons_min, FuelCons_max, Price_max),
	moto(MotoID, Type, Displ, RPM, Trans_type, Color, FuelCons, Price),
	Type = Pref_type,
	Displ @>= Displ_min, Displ @=< Displ_max,
	RPM @>= RPM_min, RPM @=< RPM_max,
	Trans_type = Pref_trans_type,
	Color = Pref_color,
	FuelCons @>= FuelCons_min, FuelCons @=< FuelCons_max,
	Price @=< Price_max.
