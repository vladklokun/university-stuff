:- include('menu.pl').

temp(X) :-
    menuask(temp, X, [hot, cold, warm]).

precipitation(X) :-
    menuask(precipitation, X, [snow, rain, none]).

sun_days(X) :-
    menuask(sun_days, X, [few, some, many]).

season(summer) :-
    temp(hot),
    sun_days(many),
    precipitation(none).

season(winter) :-
    temp(cold),
    sun_days(few),
    precipitation(snow).

season(spring) :-
    temp(hot),
    sun_days(many),
    precipitation(rain).

season(autumn) :-
    temp(cold),
    sun_days(few),
    precipitation(rain).
