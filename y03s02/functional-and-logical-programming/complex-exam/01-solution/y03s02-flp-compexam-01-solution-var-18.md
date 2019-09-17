---
title: "Комплексна контрольна робота з ФЛП"
author: "Клокун В. Д."
date: "2019-05-18"
---

# Варіант № 18

## Поясніть, яким чином при виконанні Пролог-програми визначається, до якого типу даних має належати та чи інша змінна. Наведіть приклади, що ілюструють Вашу відповідь.
За стандартом ISO/IEC 13211 мова Пролог динамічно типізована і має лише один тип даних — терм. Терми мають декілька підтипів: атоми, числа, змінні та складені терми. Самі по собі змінні не мають типу даних, натомість вони можуть бути прив'язані до значень будь-якого типу даних.

Однак, у мові Turbo Prolog тип даних, до якого має належати значення змінної, визначається у розділі `domains`, наприклад, так:
```prolog
domains
    name, surname = string
    age = integer
    height, weight = real
```
Ці типи даних потім використовуються, щоб оголосити предикати у розділі `predicates` і використати описані предикати у розділі `clauses`:
```prolog
predicates
    person(surname, name, age, height, weight)
clauses
    person("Pupkin", "Vasiliy", 44, 160, 70).
    person("Petrova", "Anna", 37, 175, 50).
    person(1, "Anna", 37, 175, 50).
```
Тоді при виконанні Пролог-програми, щоб визначити тип даних, до якого має належати значення змінної, Пролог порівняє фактичні аргументи предиката, які були описані і передані в розділі `clauses`, з прототипом використання предикату у розділі `predicates` і перевірить значення переданих аргументів з типами даних, описаними у розділі `domains`.

Отже, такий початковий код призведе до помилки:
```prolog
clauses
    % Помилка: значення «1» не належить коректному типу даних
    % surname (= string), описаному в прототипі, а належить
    % типу даних integer
    person(1, "Anna", 37, 175, 50).
```

## Поясніть різницю між зовнішніми і внутрішніми цілями Пролог-програми.
Різниця між зовнішніми і внутрішніми цілями Пролог-програми у тому, що зовнішні цілі описуються після запуску Пролог-програми в інтерактивному режимі, а внутрішні — у початковому коді Пролог-програми, для Turbo Prolog — в розділі `goals`.

## Задача. Мовою Пролог опишіть предикат `insert2(X, Y, L1, L2`, який виконує вставку елемента `X` в заданий список перед заданим елементом `Y` цього списку.
```prolog
% ISO-Prolog
% insert2(X, Y, L1, L2)
% X - елемент, який треба вставити
% Y - елемент, перед яким треба вставити елемент X
% L1 — список, у який треба вставити елемент
% L2 - список, у якому перед елементом X знаходиться елемент Y

% Якщо елемент Y знаходиться у голові початкового списку, вставити
% у результуючий список елемент X перед елементом Y
insert2(X, Y, [Y | T], [X, Y | T ]).
% Якщо елемент Y не співпадає з головою початкового списку, перейти
% до наступних елементів списку
insert2(X, Y, [H | T], [H | L ]) :-
    Y \= H,
    insert2(X, Y, T, L).
```