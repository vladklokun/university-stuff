#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
1. Знайти функцію вигляду X = F^{-1}(\xi), використовуючи метод оберненої
функції.
(Варіант №8: F(x) = x^3)

2. Побудувати імітаційну модель отримання системи неперервних випадкових
величин, що мають рівномірний розподіл на проміжку [0; 1] (використати ГПВЧ).

3. На основі отриманих значень системи неперервних випадкових величин,
в створеній програмі побудувати графік функції розподілу F(x) неперервної
випадкової величини X за методом оберненої функції.

4. Знайти ймовірність того, що неперервна випадкова величина X прийме
значення, яке належить інтервалу [a; b].
(Варіант №8: a = 0.5; b = 0.9)
"""
import math
import random
import matplotlib.pyplot as plt
import multiprocessing as mp


def split_list_of_points(lofp):
    """
    Розділяє список точок у вигляді [(x1, y1), (x2, y2), (x3, y3), ...]
    у два кортежі: x = (x1, x2, x3, ...), y = (y1, y2, y3, ...)
    """
    x, y = zip(*lofp)
    return x, y


def calc_x_in_ab_prob(f, a, b):
    r"""
    Обчислює ймовірність того, що значення зі списку `X` попадають в інтервал
    [a, b]

    :param f: початкова, не обернена функція, за якою обчислюється ймовірність
        попадання в інтервал
    :type func:
    :param a: нижня границя інтервалу (включно)
    :type float:
    :param b: верхня границя інтервалу (включно)
    :type float:
    :returns: ймовірність того, що значення попадають в інтервал $[a, b]$
    :rtype float:
    """
    # Знаходимо менше і більше значення, щоб уникнути зворотних інтервалів
    lesser_val, greater_val = sorted([a, b])
    return f(greater_val) - f(lesser_val)


def plot_prob_func(X, xi, xlabel=r'$X$', ylabel=r'$\xi$'):
    r""" Будує графік функції ймовірностей

    :param X: значення $X$ — ймовірності
    :type X: list
    :param xi: значення $\xi$ — значення, отримані з генератора
        псевдовипадкових чисел
    :type xi: list
    :param xlabel: підпис для осі абсцис
    :type str:
    :param ylabel: підпис для осі ординат
    :type str:
    """
    fig = plt.figure(1)

    ax = fig.add_subplot(111)
    ax.plot(X, xi)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    # На осі OX знаходяться значення випадкової змінної, тому для наочності
    # обмежуватимемо лише мінімальним значенням
    ax.set_xlim(min(X), None)
    # На осі OY знаходяться значення ймовірності, тому для наочності завжди
    # обмежуватимемо інтервалом [0.0, 1.0]
    ax.set_ylim(0.0, 1.0)
    plt.grid()
    plt.show()
    return


def run_lab(parent_func, inverted_func, a, b, rand_count=50):
    """
    Запускає завдання лабораторної роботи на виконання

    :param parent_func: початкова функція, задана в завданні на роботу
    :type func:
    :param inverted_func: обернена функція, обчислена власноруч
    :type func:
    :param a: нижня границя інтервалу (включно)
    :type float:
    :param b: верхня границя інтервалу (включно)
    :type float:
    :param rand_count: кількість випадкових значень, які мають бути згенеровані
        для системи неперервних випадкових величин
    :type int:
    """
    # Завдання 2: створити RAND_COUNT випадкових значень, рівномірно
    # розподілених на інтервалі [0.0, 1.0)
    print('\n# Task 2 part 1: random values')

    rand_vals = [random.random() for _ in range(rand_count)]

    print('rand_vals = {}'.format(rand_vals))

    # Створити систему неперервних випадкових змінних, такого вигляду
    # (<випадкова змінна>, <значення оберненої функції для випадкової змінної>)
    print('\n# Task 2 part 2: system of continuous random variables')
    system_crv = sorted([(val, inverted_func(val)) for val in rand_vals])

    # Вивести заголовок для системи неперервних випадкових змінних
    print('{:->14}'.format(''))
    print('{:>6} |{:>6}'.format('xi', 'X'))
    print('{:->14}'.format(''))

    # Print xi, X values in the system
    # Вивести значення $\xi$, $X$ із СНВВ
    for xi, X in system_crv:
        print('{:.4f}, {:.4f}'.format(xi, X))

    xi, X = split_list_of_points(system_crv)

    # Завдання 3: побудувати графік функції ймовірностей
    print('\n# Task 3: plot the probability function'
          '\n(Running in the background)')

    # Create a process for plotting the function
    # Створюємо процес для побудови графіку функції
    p = mp.Process(
        target=plot_prob_func,
        args=(X, xi,
              r'Неперервна випадкова величина $X$',
              r'$F(X)$')
    )
    p.start()  # Запускаємо створений процес фоном

    # Завдання 4: визначити ймовірність, що величини з $X$ попадають в інтервал
    # $[a, b]$
    print('\n# Task 4: probability that X is in [a; b]')
    p = calc_x_in_ab_prob(parent_func, a, b)
    print('p(X in [{}, {}]) = {}'.format(a, b, p))


def main():
    # Оголошуємо параметри, дані у завданні варіанта
    def parent_func(x): return math.sqrt(x)
    a, b = 0.2, 0.8

    # Завдання 1: визначити обернену функцію
    #
    # \xi = \sqrt(x)
    # \xi^2 = x
    # x = \xi^2
    def inv_func(x): return x**2

    # Запустити моделювання із заданими у варіанті параметрами та 100
    # випадковими величинами
    run_lab(parent_func, inv_func, a, b, rand_count=100)


if __name__ == '__main__':
    main()
