domains
    icecrm_id, store_id, icecrm_type = symbol
    icecrm_name = string
    icecrm_weight, icecrm_price = real
    stock = symbol*

predicates
    icecream(icecrm_id, icecrm_type, icecrm_name, icecrm_weight,
             icecrm_price)
    store(store_id, stock)
    icecrm_in_stock(icecrm_id, stock)
    store_has_icecrm(store_id, icecrm_id)
    store_icecrm_weight_over(store_id, icecrm_id, icecrm_weight)

clauses
    % морозиво(ID морозива, ім'я, вага, ціна).
    % ID морозива = maxm100 — (Max)i(m)use, (100) g
    % sandwich — брикет, cone — ріжок, bar — ескімо
    icecream(maxm090, sandwich, "Maximuse", 90.0, 18.0).
    icecream(choc100, cone, "Three Chocolates", 100.0, 35.0).
    icecream(mona080, bar, "Monaco Cookies", 80.0, 25.0).
    icecream(sush070, cone, "Super Chocolate", 70.0, 25.0).

    % магазин(ID магазину, [асортимент магазину за ID]).
    store(s0, [maxm090, choc100, mona080, sush070]).
    store(s1, [maxm090, mona080, sush070]).
    store(s2, [choc100, sush070]).

    % Рекурсивна перевірка, чи є морозиво в наявності
    % icecrm_in_stock(ID морозива, наявність)
    icecrm_in_stock(IceCrmID, [IceCrmID | _]).
    icecrm_in_stock(IceCrmID, [_ | T]) :-
        icecrm_in_stock(IceCrmID, T).

    % Перевірка, чи є морозиво IceCrmID у магазині StoreID
    store_has_icecrm(StoreID, IceCrmID) :-
        store(StoreID, Stock),
        icecrm_in_stock(IceCrmID, Stock).

    % Пошук морозива у магазині, яке важить більше за Weight
    % Запит, щоб знайти морозиво в магазині s0, важчі за 80:
    % store_icecrm_weight_over(s0, IceCrmID, 80).
    store_icecrm_weight_over(StoreID, IceCrmID, Weight) :-
        % Знайти асортимент магазину Stock
        store(StoreID, Stock),
        % Знайти морозиво IceCrmID в асортименті
        icecrm_in_stock(IceCrmID, Stock),
        % Знайти ціну морозива
        icecream(IceCrmID, _, IceCrmWeight, _),
        % Істина, якщо вага більше заданої
        IceCrmWeight > Weight.
