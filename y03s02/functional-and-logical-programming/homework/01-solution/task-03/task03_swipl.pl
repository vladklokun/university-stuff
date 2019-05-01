% Solution for SWI Prolog
% moto(Vendor, Type, Engine_Capacity, RPM, Transmisison, Color, MPG, Price).
% moto(Vendor, Type, Engine_Capacity, RPM, FuelType, Price)
moto(honda, scooter, 2000, 12000, gasoline, 10000).
moto(yamaha, scooter, 2000, 12000, gasoline, 10000).
moto(suzuki, bike, 2000, 12000, gasoline, 10000).

% client(
% 	Name, Type, EC_min, EC_max, RPM_min, RPM_max, tran_type, color,
% 	fuel_cons_min, fuel_cons_max, price
% )
client(john, scooter, 0, 0, 0, 0).
client(mark, bike, 0, 0, 0, 0).
client(mark, bike, 0, 0, 0, 0).
client(mark, bike, 0, 0, 0, 0).
client(mark, bike, 0, 0, 0, 0).
client(mark, bike, 0, 0, 0, 0).
client(clark, atv, 0, 0, 0, 0).
client(clark, atv, 0, 0, 0, 0).
client(clark, atv, 0, 0, 0, 0).
client(kent, scooter, 0, 0, 0, 0).
client(kent, scooter, 0, 0, 0, 0).
client(kent, scooter, 0, 0, 0, 0).
client(sid, bike, 0, 0, 0, 0).

has_type(X, Type) :-
	moto(X, Type, _, _, _, _).

wants_type(Client, Type) :-
% Checks if client Client wants type Type
	client(Client, Type, _, _, _, _).

count_type_preferences(Type, C) :-
% Counts how many clients want type Type
	findall(_, wants_type(_, Type), Z),
	length(Z, C).

append_scooter_count(L, L2) :-
	% Double square brackets to append as list
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

% Define comparators for [Type, Count] pairs to use with predsort/2
% type_count_cmp(>, [_, Count1], [_, Count2]) :-
%	Count1 > Count2.

%type_count_cmp(<, [_, Count1], [_, Count2]) :-
%	Count1 < Count2.

%type_count_cmp(=, [_, Count1], [_, Count2]) :-
%	Count1 = Count2.
%

%sort_type_prefs(L, RL) :-
%	predsort(type_count_cmp, L, RL).

get_sorted_type_prefs(L, RL) :-
	count_all_type_prefs(L, L1),
	keysort(L1, L2),
	reverse(L2, RL).

% Figure out how to get a head of passed list
get_most_popular_pref([H | _], H).
