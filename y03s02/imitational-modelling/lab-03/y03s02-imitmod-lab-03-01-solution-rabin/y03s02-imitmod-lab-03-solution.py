#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Завод відправив на базу n деталей. Ймовірність пошкодження деталей при
перевезенні дорівнює 0.03. Побудувати ряд розподілу для числа X --- кількості
пошкоджених в дорозі деталей (перших 10). Скористатись розподілом Пуассона.
"""


import numpy as np
import scipy.stats as sp_stats
import matplotlib.pyplot as plt


def split_list_of_points(lofp):
    lx, ly = zip(*lofp)
    return lx, ly


def print_distr_series(pos_vals, pmf):
    print('{:>10} {:>10}'.format('X', 'P'))
    for pos_val, pmf in zip(pos_vals, pmf):
        print('{:10.6f} {:10.6f}'.format(pos_val, pmf))


def main():
    n = float(input('Введіть кількість деталей n: '))
    p_n_corrupt = float(
        input(
            'Введіть ймовірність пошкодження деталі при перевезенні p(n_corrupt)\n'
            '(за текстом завдання --- 0.03): '
        )
    )
    show_amount = float(
        input(
            'Введіть, скільки перших деталей зображати\n'
            '(за текстом завдання --- 10): '
        )
    )

    # Можливі значення pos_vals --- кількість деталей, що вийшли з ладу.
    # Функція np.arange(x) створює ітератор до значення `x` виключно, тому +1
    # компенсує цю поведінку
    pos_vals = np.arange(show_amount)
    # Отримуємо значення функції розподілу ймовірностей --- pmf
    pmf = sp_stats.poisson.pmf(pos_vals, p_n_corrupt)

    # Виводимо ряд розподілу
    print('\n# Завдання №1: ряд розподілу випадкової величини')
    print_distr_series(pos_vals, pmf)

    # Завдання №2: графік функції ймовірностей і многокутник розподілу
    print('\n# Завдання №2: графік функції ймовірностей '
          'і многокутник розподілу')

    # Фукція ймовірностей --- залежність ймовірності (по OY)
    # від можливого значення (по OX)
    x, y = pos_vals, pmf

    # Будуємо графік функції ймовірностей
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    ax.set_xlim(0.0, None)
    ax.set_ylim(0.0, 1.0)
    ax.set_xlabel('Кількість пошкоджених деталей')
    ax.set_ylabel('Ймовірність $F(X)$')
    plt.grid()

    # Будуємо многокутник розподілу

    # Для правильної побудови многокутника створюємо список точок,
    # відсортованих за значеннями по осі OX --- ймовірністю
    points = [i for i in sorted(zip(pmf, pos_vals))]

    # Розбиваемо список точок на два кортежі зі значеннями для кожної осі:
    # pos_vals, pmf
    pmf, pos_vals = split_list_of_points(points)

    # Многокутник розподілу --- залежність можливої величини (по OY)
    # від ймовірності (по OX)
    x, y = pmf, pos_vals

    # Будуємо сам многокутник розподілу
    fig = plt.figure(2)
    ax = fig.add_subplot(111)

    ax.plot(x, y)
    ax.set_xlim(0.0, None)
    ax.set_ylim(0.0, None)
    ax.set_xlabel('Ймовірність $P$')
    ax.set_ylabel('Кількість пошкоджених деталей')
    plt.grid()

    plt.show()

    return


if __name__ == '__main__':
    main()
