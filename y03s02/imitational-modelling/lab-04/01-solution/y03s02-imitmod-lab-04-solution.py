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
import random
import matplotlib.pyplot as plt
import multiprocessing as mp


def split_list_of_points(lofp):
    """
    Splits a list of points of form [(x1, y1), (x2, y2), (x3, y3), ...]
    into [x1, x2, x3, ...], [y1, y2, y3, ...]
    """
    lx, ly = zip(*lofp)
    return lx, ly


def calc_x_in_ab_prob(X, a, b):
    r"""
    Calculates probability of values in list `X` belonging to the interval
    [a, b]

    :param X: a list of numerical values
    :type list:
    :param a: lower interval bound (inclusive)
    :type float:
    :param b: upper interval bound (inclusive)
    :type float:
    :returns: probability that $X \in [a, b]$
    """
    count = 0
    total = len(X)
    for x in X:
        if a <= x <= b:
            count += 1
    return count / total


def plot_prob_func(X, xi):
    """ Plots probability function
    :param X: X values
    :type X: list
    :param xi: xi values
    :type xi: list
    """
    fig = plt.figure(1)

    ax = fig.add_subplot(111)
    ax.plot(X, xi)
    ax.set_xlabel(r'$X$')
    ax.set_ylabel(r'$\xi$')
    ax.set_xlim(0.0, None)
    plt.grid()
    plt.show()
    return


def run_lab(func, a, b):
    # Task 2: Create RAND_COUNT random values uniform on [0.0, 1.0)
    print('\n# Task 2 part 1: random values')

    RAND_COUNT = 10
    rand_vals = [random.random() for _ in range(RAND_COUNT)]

    print('rand_vals = {}'.format(rand_vals))

    # Create a system of continuous random variables with their function values
    print('\n# Task 2 part 2: system of continuous random variables')
    system_crv = sorted([(val, func(val)) for val in rand_vals])

    # Print header
    print('{:->14}'.format(''))
    print('{:>6} |{:>6}'.format('xi', 'X'))
    print('{:->14}'.format(''))

    # Print xi, X values in the system
    for xi, X in system_crv:
        print('{:.4f}, {:.4f}'.format(xi, X))

    xi, X = split_list_of_points(system_crv)

    # Task 3: Probability function
    print('\n# Task 3: plot the probability function'
          '\n(Running in the background)')

    # Create a process for plotting the function
    p = mp.Process(target=plot_prob_func, args=(X, xi))
    p.start()  # run it in the background

    # Task 4: prob(X \in [a; b])
    print('\n# Task 4: probability that X is in [a; b]')
    p = calc_x_in_ab_prob(X, a, b)
    print('p(X in [{}, {}]) = {}'.format(a, b, p))


def main():
    # Declare parameters given in the task's variant
    a, b = 0.5, 0.9

    # Task 1: figure out the inverse function
    #
    # \xi = x^3
    # \xi^{1/3} = x
    # x = \xi^{1/3}
    def func(x): return x**(1/3)

    # Run the tasks with given parameters
    run_lab(func, a, b)


if __name__ == '__main__':
    main()
