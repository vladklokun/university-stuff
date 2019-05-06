#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import multiprocessing as mp
import matplotlib.pyplot as plt


class Model(object):
    """ A class that represets a process model
    """

    def __init__(self, functional_law, delta_t_min, delta_t_max,
                 delta_t=None, **kwargs):
        """
        :param functional_law: A function that describes how a model
            behaves in time
        :type functional_law: func
        :param delta_t_min: lower bound for randomly generating delta_t
        :type delta_t_min: float
        :param delta_t_max: upper bound for randomly generating delta_t
        :type delta_t_max: float
        :param delta_t: explicit delta_t value. Overrides generated one.
        :type delta_t: float
        """
        # The functional law itself
        self.functional_law = functional_law
        # Variables neccessary for the functional_law to be computed
        self.functional_law_vars = kwargs
        # Time step
        self.delta_t = random.uniform(delta_t_min, delta_t_max)
        # If delta_t is explicitly passed, override it
        if delta_t:
            self.delta_t = delta_t

    def run(self, t):
        """
        Run the model at time point "T"

        :param t: time point value
        :type t: float

        :return: time point t and the value of a system in time point t
        :rtype: tuple
        """
        return t, self.functional_law(**self.functional_law_vars, t=t)

    def run_for(self, time):
        """
        A generator function that runs a model for a given duration `time`

        :param time: time duration how long a model should be run
        :type time: float
        """
        t = 0
        while t < time:
            yield self.run(t)
            t += self.delta_t


def split_list_of_points(lofp):
    """ Splits a list of points of form [(x1, y1), (x2, y2), (x3, y3), ...]
    into [x1, x2, x3, ...], [y1, y2, y3, ...]
    """
    lx, ly = zip(*lofp)
    return lx, ly


def print_table(t, colh1='x', colh2='y'):
    # Accomodate for two values and a separator
    print('{:->33}'.format(''))
    print('{:>15} | {:>15}'.format(colh1, colh2))
    print('{:->33}'.format(''))
    for x, y in t:
        print('{:+15.4f} | {:+15.4f}'.format(x, y))
    print('{:->33}'.format(''))


def plot_func(x, y, xlabel='x', ylabel='f(x)'):
    fig = plt.figure(1)

    ax = fig.add_subplot(111)
    ax.plot(x, y)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xlim(0.0, None)
    plt.grid()
    plt.show()
    return


def main():
    # Описуємо функцію, задану в завданні за варіантом
    def f(t): return 0.3*t - 1180

    # Зчитуємо тривалість часу
    t = float(input('Введіть бажану тривалість роботи системи t: '))

    # Run the system
    # Pass every needed variable as a keyword argument
    # Завдання 1: моделювання системи
    print('\n# Завдання 1: моделювання системи')

    # Створюємо об'єкт-систему з параметрами, від яких залежить функція
    # Ці параметри (дельта t та змінні, від яких залежить функція) описані
    # у завданні
    model = Model(f, delta_t_min=0, delta_t_max=1)

    # Запускаємо модель на час t і будуємо таблицю результатів симуляції
    # за отриманими даними
    simulation_table = [x for x in model.run_for(time=t)]

    # Виводимо створену таблицю
    print_table(simulation_table)

    # Розбиваємо таблицю на окремі кортежі: координати x і y відповідно.
    # Це потрібно для побудови графіка траекторії процесу
    x, y = split_list_of_points(simulation_table)

    # Завдання 2: побудувати графік траекторії процесу
    print('\n# Завдання 2: побудова графіку траекторії процесу'
          '\n(Виконується у фоновому режимі)')

    # Створюємо окремий процес для побудови графіка траекторії процесу,
    # що імітується
    p = mp.Process(
        target=plot_func,
        args=(x, y),
        # Задаємо підписи для осей OX, OY відповідно
        kwargs={
            'xlabel': 't',
            'ylabel': 'y(t)'
        }
    )
    # Запускаємо створений процес --- будуємого графік траекторії процесу
    p.start()


if __name__ == '__main__':
    main()
