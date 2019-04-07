#!/usr/bin/env python3


import random  # random.uniform()


class Subsystem(object):
    def __init__(self, p_faultless=0.0, failed=False):
        self.p_faultless = p_faultless
        self.failed = failed

    def set_p_faultless(self, new_p):
        self.p_faultless = new_p

    def set_failed(self):
        self.failed = True

    def print_info(self):
        print(
            'P(faultless) = {}, Failed = {}'
            .format(self.p_faultless, self.failed)
        )

    def has_failed(self):
        return self.failed


class System(object):
    def __init__(self, subsystems=[]):
        self.subsystems = subsystems

    def add_subsystem(self, subsystem):
        self.subsystems.append(subsystem)

    def print_state(self):
        state = [s.has_failed() for s in self.subsystems]
        print(state)

    def run_round(self):
        for s in self.subsystems:
            cur_rand = random.uniform(0.0, 1.0)
            if cur_rand > s.p_faultless:
                s.set_failed()

    def run_rounds(self, round_cnt):
        for r in range(round_cnt):
            print('### Round {}'.format(r))
            self.run_round()
            self.print_state()


def main():
    subsystems = [Subsystem(random.uniform(0.9, 1.0)) for x in range(2)]

    sys1 = System(subsystems)
    sys1.run_rounds(20)


if __name__ == '__main__':
    main()

