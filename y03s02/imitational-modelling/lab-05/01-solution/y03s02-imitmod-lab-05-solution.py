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
    print('{:->6} {:->6}'.format(colh1, colh2))
    for x, y in t:
        print('{:02.4f}, {:02.4f}'.format(x, y))


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
    # Declare the function described in the task
    def f(t, V_1, V_2, v, m): return (V_1 * (v-V_2)) / (m+t)**2

    # Read the time duration
    t = float(input('Введіть бажану тривалість роботи системи t: '))

    # Read the needed parameters from stdin
    V_1 = float(input('Введіть значення V_1: '))
    V_2 = float(input('Введіть значення V_2: '))
    v = float(input('Введіть значення v: '))
    m = float(input('Введіть значення m: '))

    # Run the system
    # Pass every needed variable as a keyword argument
    print('\n# Task 1: Modelling the system')

    sys = Model(f, 0, 1, V_1=V_1, V_2=V_2, v=v, m=m)
    simulation_table = [x for x in sys.run_for(time=t)]
    print_table(simulation_table)
    x, y = split_list_of_points(simulation_table)

    # Task 2: Plot process trajetory
    print('\n# Task 2: plot the process trajectory'
          '\n(Running in the background)')

    p = mp.Process(target=plot_func, args=(x, y))
    p.start()


if __name__ == '__main__':
    main()
