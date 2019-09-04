% Обгортка для предиката findmax_3 на 2 параметри
findmax([H | T], Res) :-
    findmax_3(T, H, Res).

% Термінальна вітка: для пустого списку максимумом будуть передані
% параметри
findmax_3([], R, R).
% Якщо поточний елемент більше поточного максимуму CurMax, змінити
% поточний максимум CurMax на поточний елемент H і шукати максимум
% у хвості списку
findmax_3([H | T], CurMax, Res) :-
    H > CurMax,
    findmax_3(T, H, Res).
% Інакше не змінювати максимум і шукати у хвості списку
findmax_3([H | T], CurMax, Res) :-
    H =< CurMax,
    findmax_3(T, CurMax, Res).

% Оболонка для єдиного параметра
list_from_stdin(R) :-
    list_from_stdin([], R).
% Зчитує дані, що вводить користувач. Елементи додаються у початок
% списку
list_from_stdin(InList, OutList) :-
    writeln("Please enter a number (or anything else to stop):"),
    read(Input),
    % Перевірити, чи є введені дані числом
    (
        integer(Input)
    ;   float(Input)
    ),
    % Додати елемент у початок списку
    list_from_stdin([Input | InList], OutList).
% Якщо введені дані не були числом, вивести поточний список.
list_from_stdin(L, L).

main :-
    list_from_stdin(L),
    write("Your list: "),
    writeln(L),
    findmax(L, Max),
    write("Max in your list: "),
    writeln(Max).
