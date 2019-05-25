domains
    ilist = integer*
    index = integer

predicates
    run
    readlist(ilist)
    length(ilist, integer)
    length_3(ilist, integer, integer)
    append(ilist, ilist, ilist)
    sort_list(ilist, ilist)
    mergesort(ilist, ilist)
    merge(ilist, ilist, ilist)
    split_in_half(ilist, ilist, ilist)
    split_at(ilist, index, ilist, ilist)
    not_in(integer, ilist)
    no_duplicates(ilist)
    is_not_min_or_max(integer, ilist)

goal
    run.

clauses
    % Зчитує список, який вводить користувач
    readlist([X|Xs]) :-
        readint(X),
        !,
        readlist(Xs).
    % Завершити роботу, якщо список пустий. Використовується для виходу
    % з рекурсії: коли користувач вводить не ціле число, хвіст стає пустим
    % і предикат завершує роботу.
    readlist([]).

    % Обгортка для визначення довжини списку
    length(L, Len) :-
        % Викликаємо предикат з аккумулятором зі значенням 0
        length_3(L, 0, Len).

    % Визначення довжини списку за допомогою аккумулятора `Acc`
    length_3([], Len, Len).
    length_3([_|Xs], Acc, Len) :-
        NewAcc = Acc + 1,
        length_3(Xs, NewAcc, Len).

    % Додає зміст Списку 2 до змісту Списку 1 в результуючий Список 3
    append([], L, L).
    append([X|Xs], L, [X|Ys]) :-
        append(Xs, L, Ys).

    % Обгортка для сортування списку
    sort_list(X, Y) :-
        mergesort(X, Y).

    % Сортування злиттям
    mergesort([], []).
    mergesort([L], [L]).
    mergesort([H|T], Res) :-
        length(T, Len),
        % Якщо список має хоча б один елемент
        Len > 0,
        % Розділити його навпіл
        split_in_half([H|T], Half1, Half2),
        % І відсортувати злиттям кожну половину
        mergesort(Half1, Res1),
        mergesort(Half2, Res2),
        % А потім об'єднати в єдиний відсортований список
        merge(Res1, Res2, Res),
        % Відсікання, щоб знайти єдиний розв'язок
        !.

    % Зливає два списки для сортування злиттям
    merge([], L, L).
    merge(L, [], L).
    % Якщо значення елемента X менше за значення елемента Y, помістити його
    % перед елементом Y у результуючий список
    merge([X|Xs], [Y|Ys], [X|TR]) :-
        X <= Y,
        merge(Xs, [Y|Ys], TR).
    % Якщо значення елемента Y менше за значення елемента X, помістити його
    % перед елементом X у результуючий список
    merge([X|Xs], [Y|Ys], [Y|TR]) :-
        Y <= X,
        merge([X|Xs], Ys, TR).

    % Розподіляє список навпіл
    split_in_half(L, Half1, Half2) :-
        length(L, Len),
        % Розподілити довжину списку навпіл, розділивши її націло (div —
        % ділення націло)
        HalfIdx = Len div 2,
        split_at(L, HalfIdx, Half1, Half2).

    % Розділяє список `L` за індексом `Idx` на два списки: `Part1` і `Part2`
    split_at(L, Idx, Part1, Part2) :-
        % Якщо довжина першої частини — `Idx`...
        length(Part1, Idx),
        % ...і після об'єднання списки `Part1` та `Part2` сформують список `L`,
        % списки розподілені як треба
        append(Part1, Part2, L).

    % Істина, якщо елемента `X` немає в списку `L`
    not_in(_, []).
    not_in(X, [Y|Ys]) :-
        X <> Y,
        not_in(X, Ys).

    % Істина, якщо в списку немає повторюючихся елементів
    no_duplicates([]).
    no_duplicates([X|Xs]) :-
        not_in(X, Xs),
        no_duplicates(Xs).

    % Істина, якщо L — 3-елементний список, в якому елемент `B`
    % є ні мінімальним, ні максимальним елементом
    is_not_min_or_max(B, L) :-
        length(L, 3),
        no_duplicates(L),
        % Щоб знайти мінімальний і максимальний елемент, відсортувати список
        sort_list(L, [_, B, _ | []]),
        % Відсікання, щоб знайти лише один розв'язок
        !.

    % Запускає програму
    run :-
        makewindow(1, 7, 7, "Input Window", 1, 1, 20, 35),
        write(
            "Please enter a list of integers\n",
            "separated by <Enter>. The list\n",
            "must contain exactly 3 elements.\n",
            "Duplicates are forbidden.\n",
            "When you're done with the list,\n",
            "type 'q'.\n",
            "List:\n"
        ),
        readlist(InList),
        % Якщо користувач вводить некоректний список, предикат
        % `is_not_min_or_max/2` не буде істиним — переходимо до виводу помилки.
        is_not_min_or_max(Res, InList),
        makewindow(2, 7, 7, "Output Window", 1, 36, 20, 35),
        write("Not min or max: ", Res).

    % Якщо `is_not_min_max/2` не був істиним, тобто користувач ввів список,
    % що складається не з 3 елементів або список, який містить повторення,
    % вивести повідомлення про помилку
    run :-
        makewindow(2, 7, 7, "Output Window", 1, 36, 20, 35),
        write("Invalid input.").
