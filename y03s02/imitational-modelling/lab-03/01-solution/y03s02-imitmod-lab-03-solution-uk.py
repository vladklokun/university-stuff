#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
В партії з n_1 деталей є n_2 стандартних деталей. Навмання із всієї партії
вибирається 2 деталі. Побудувати ряд розподілу числа X — числа стандартних
деталей серед відібраних. Скористатись гіпергеометричним розподілом.
"""


import numpy as np
import scipy.stats as sp_stats
import matplotlib.pyplot as plt


def split_list_of_points(lofp):
    lx, ly = zip(*lofp)
    return lx, ly


def main():
    n_1 = float(input('Введіть кількість деталей в партії n_1: '))
    n_2 = float(input('Введіть кількість стандартних деталей n_2: '))
    num_samples = float(input(('Введіть, скільки деталей буде обрано: ')))

    total = n_1  # Загальна кількість випадків
    good = n_2   # Кількість сприятливих подій

    rand_var = sp_stats.hypergeom(total, good, num_samples)
    possible_outcomes = np.arange(num_samples+1)
    # pmf --- probability mass function --- функція ймовірностей
    pmf_details = rand_var.pmf(possible_outcomes)

    # Графік функції ймовірності
    fig = plt.figure(1)

    ax = fig.add_subplot(111)
    ax.plot(possible_outcomes, pmf_details, 'bo')
    # Побудувати вертикальні лініі від 0 значення ймовірності
    ax.vlines(possible_outcomes, 0, pmf_details, lw=2)
    ax.set_xticks(possible_outcomes)
    ax.set_xlim(0.0, None)
    ax.set_ylim(0.0, 1.0)
    ax.set_xlabel('Кількість стандартних деталей серед обраних')
    ax.set_ylabel('Ймовірність F(X)')
    plt.grid()

    # Графік многокутника розподілу
    fig = plt.figure(2)
    plt.subplot(111)
    ax = fig.add_subplot(111)
    # Створюємо список усії точок графіка, відсортованих за значенням
    # імовірності X
    points = [i for i in sorted(zip(pmf_details, possible_outcomes))]
    # Розділяємо список точок на окремі кортежі x і y, які містять координати
    # X, Y відповідно
    x, y = split_list_of_points(points)
    ax.plot(x, y)
    ax.set_xlim([0.0, None])
    ax.set_ylim([0.0, None])
    ax.set_xticks(np.arange(1.1, step=0.1))
    ax.set_xlabel('Ймовірність P(X)')
    ax.set_ylabel('Кількість стандартних деталей\nсеред обраних')

    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
