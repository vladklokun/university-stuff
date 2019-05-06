domains
    bev_id, store_id, bev_type = symbol
    bev_name = string
    bev_volume, bev_price = real
    stocklist = symbol*

% Створюємо динамічну базу даних `stores` —
% список існуючих магазинів, де визначений предикат `store`
database - stores
    store(store_id, stocklist)

predicates
    beverage(bev_id, bev_type, bev_name, bev_volume, bev_price)
    bev_in_stocklist(bev_id, stocklist)
    store_has_bev(store_id, bev_id)
    store_bev_under(store_id, bev_id, bev_price)
    buy_bev_one(bev_id, stocklist, stocklist)
    buy_store_bev(store_id, bev_id)

clauses
    % напій(ID напою, ім'я, тривалість виконання (с)).
    % ID напою = jd05 — (J)ack (D)aniels, (0.5) L
    beverage(jd05, whiskey, "Jack Daniels", 0.5, 100.0).
    beverage(jb05, whiskey, "Jim Beam", 0.5, 100.0).
    beverage(bl05, liqueur, "Bailey's", 0.5, 75.0).
    beverage(pl05, beer, "Paulaner", 0.5, 25.0).

    % магазин(ID магазину, [асортимент магазину за ID]).
    store(s0, [jd05, jb05, bl05, pl05]).
    store(s1, [jb05, jd05, pl05]).
    store(s2, [jb05, bl05, pl05]).

    % Рекурсивна перевірка, чи є напій в списку наявності
    % bev_in_stocklist(напій, наявність)
    bev_in_stocklist(Bev, [Bev | _]).
    bev_in_stocklist(Bev, [_ | T]) :-
        bev_in_stocklist(Bev, T).

    % Перевірка, чи є напій BevID у магазині StoreID
    store_has_bev(StoreID, BevID) :-
        store(StoreID, Stocklist),
        bev_in_stocklist(BevID, Stocklist).

    % Пошук напоїв у магазині, які коштують дорожче за Price
    % Запит, щоб знайти напої в магазині s0, дешевші за 35:
    % store_bev_under(s0, Bev, 35).
    store_bev_under(StoreID, BevID, Price) :-
        % Знайти асортимент магазину Stocklist
        store(StoreID, Stocklist),
        % Знайти напій BevID в асортименті
        bev_in_stocklist(BevID, Stocklist),
        % Знайти ціну напою
        beverage(BevID, _, _, _, BevPrice),
        % Істина, якщо ціна менше заданої
        BevPrice < Price.

    % Рекурсивний предикат, щоб купити один напій Item
    % з асортименту (видалити перший елемент `Item` зі
    % списку)
    buy_bev_one(_, [], []).
    % Відсікання, щоб отримувати лише один результат
    buy_bev_one(Item, [Item | Tail], Tail) :- !.
    buy_bev_one(Item, [Head | Tail], [Head | Res]) :-
        buy_bev_one(Item, Tail, Res).

    % Придбати напій `BevID` в магазині `StoreID`
    % Якщо напій придбали, він видаляється з асортименту
    buy_store_bev(StoreID, BevID) :-
        store(StoreID, Stocklist),
        buy_bev_one(BevID, Stocklist, NewStocklist),
        retract(
               store(StoreID, _)
        ),
        % Додати магазин StoreID з асортиментом Stocklist
        % в кінець динамічної БД `stores`
        assertz(
               store(StoreID, NewStocklist)
        ).
