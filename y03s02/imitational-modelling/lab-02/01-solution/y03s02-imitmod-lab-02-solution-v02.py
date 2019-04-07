#!/usr/bin/env python3

import random  # random.random(), random.uniform()


class Subsystem(object):
    """ Subsystem --- основний клас-підсистема для завдань №№1, 2
    """
    def __init__(self, p_faultless=0.0, failed=False):
        self._p_faultless = p_faultless
        self._failed = failed

    def __str__(self):
        """ Визначає представлення об'єкту даного класу у вигляді рядка """
        s = (
            '<SubSys at {}: P(faultless) = {}, Failed = {}>'
            .format(id(self), self.p_faultless, self.failed)
        )

        return s

    @property
    def p_faultless(self):
        """ Ймовірність безвідмовної роботи """
        return self._p_faultless

    @p_faultless.setter
    def p_faultless(self, value):
        """ Дозволяє задати значення ймовірності безвідмовної роботи """
        self._p_faultless = value

    @property
    def failed(self):
        """ Статус, що система непрацездатна """
        return self._failed

    @failed.setter
    def failed(self, value):
        self._failed = value

    def _fail(self):
        """ Робить систему непрацездатною """
        self.failed = True

    def run(self):
        """ Запускає систему у даний момент часу.

        Якщо система вже непрацездатна, завершити роботу і повернути статус
        непрацездатності. Інакше перевірити, чи зламається система у даний
        момент часу і також повернути статус непрацездатності.
        """
        if self.failed:
            return self.failed
        elif random.random() > self.p_faultless:
            self._fail()

        return self.failed


class SystemType1(object):
    """ Система з незалежними підсистемами """
    def __init__(self, subsystems=None):
        self._subsystems = subsystems

    def __str__(self):
        s = ''
        subsys_list = [str(subsys) for subsys in self.subsystems]
        s = '\n'.join(subsys_list)
        s = (
            '<System at {}:\n'
            '{}>'.format(id(self), s)
        )

        return s

    @property
    def subsystems(self):
        return self._subsystems

    def add_subsystem(self, subsystem):
        self.subsystems.append(subsystem)

    def run(self, time=1):
        for t in range(time):
            for s in self.subsystems:
                s.run()

            print('Time = {}, State = {}\n'.format(t, str(self)))

    def get_state(self):
        state = ''
        for s in self.subsystems:
            state += ''.format(str(s))

        return state


class SubsystemDependant(Subsystem):
    """ Залежна система для завдання №2.

    Успадковує та розширює незалежну підсистему
    """
    def __init__(self, p_faultless=0.0, p_faultless_leader_failed=0.0,
                 failed=False):
        self._p_faultless = p_faultless
        self._failed = failed

        self._p_faultless_leader_failed = p_faultless_leader_failed

    @property
    def p_faultless_leader_failed(self):
        return self._p_faultless_leader_failed

    @p_faultless_leader_failed.setter
    def p_faultless_leader_failed(self, value):
        self._p_faultless_leader_failed = value

    def run_leader_faulty(self):
        """ Метод, який описує процес роботи підсистеми у системі, де її головна
        підсистема непрацездатна
        """
        if self.failed:
            return self.failed
        elif random.random() > self.p_faultless_leader_failed:
            self._fail()

        return self.failed


class SystemType2(object):
    """ Система із головною і залежною підсистемою для
    завдання 2
    """
    def __init__(self, leader, dependant):
        """ Конструктор
        """
        self.subsys_leader = leader
        self.subsys_dependant = dependant

    def __str__(self):
        """ Визначає, як об'єкт даного класу виглядатиме у вигляді рядка
        """
        s = (
            '<SystemT2 at {}\n'
            'L: {},\n'
            'D: {}>'
            .format(id(self), self.subsys_leader, self.subsys_dependant)
        )
        return s

    def run_once(self):
        """ Запускає систему в один момент часу """
        # Запустити незалежну підсистему
        self.subsys_leader.run()
        # Якщо незалежна підсистема не зламалась, запустити залежну у звичайному
        # режимі
        if not self.subsys_leader.failed:
            self.subsys_dependant.run()
        # Інакше --- у режимі зламаної головної підсистеми
        else:
            print('Leader failed.')
            self.subsys_dependant.run_leader_faulty()

    def run(self, time=1):
        for t in range(time):
            self.run_once()
            print(
                'Time = {}, System = {}'
                .format(t, str(self))
            )


def main():
    runtime = int(input('Скільки часу моделювати? t = '))
    n_cnt = int(input('Скільки незалежних підсистем моделювати? n_cnt = '))
    # Завдання 1
    print('\n# Завдання №1: система з незалежними підсистемами')

    # Створюємо незалежні підсистеми
    subsystems = [
        Subsystem(p_faultless=random.uniform(0.8, 0.9))
        for _ in range(n_cnt)
    ]
    # Створюємо систему з незалежних підсистем
    system1 = SystemType1(subsystems)
    # Запускаємо її
    system1.run(time=runtime)

    # Завдання 2
    print('\n# Завдання №2: система із залежними підсистемами')

    # Створюємо систему з головною і залежною підсистемою
    system2 = SystemType2(
        # Головна
        leader=Subsystem(p_faultless=random.uniform(0.8, 0.9)),
        # Залежна
        dependant=SubsystemDependant(
            # Ймовірність безвідмовної роботи, коли головна система справна
            p_faultless=random.uniform(0.8, 0.9),
            # Ймовірність безвідмовної роботи, коли головна система несправна
            p_faultless_leader_failed=random.uniform(0.6, 0.8)
        ),
    )
    # Запускаємо її
    system2.run(time=runtime)


if __name__ == '__main__':
    main()
