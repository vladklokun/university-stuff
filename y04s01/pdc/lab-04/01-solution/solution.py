import threading
import logging

logging.basicConfig(level=logging.DEBUG)


THREAD_COUNT = 4


class Expression(object):

    def __init__(self, d, MX, R, E, allmax=None):
        self.d = d
        self.d_ready = threading.Condition()
        self.d_set = False

        self.MX = MX
        self.MX_ready = threading.Condition()
        self.MX_set = False

        self.R = R
        self.E = E
        self.E_ready = threading.Condition()
        self.E_set = False

        self.allmax = None
        self.allmax_ready = threading.Condition()
        self.allmax_set_finished = False

        self.max_counter = THREAD_COUNT
        self.max_counter_cv = threading.Condition()

        self._Z = None
        self.Z_input = threading.Condition()

    @property
    def all_max_tried(self):
        return self.max_counter == 0

    @property
    def Z(self):
        return self._Z

    @Z.setter
    def Z(self, val):
        logging.debug("Setting Z")
        with self.Z_input:
            self._Z = val
            self.Z_input.notify_all()

    def set_max(self, val):
        with self.Z_input:
            while not self.Z:
                logging.debug("Z not set. Z: {}".format(self.Z))
                self.Z_input.wait()

            with self.allmax_ready:
                logging.debug("Decrementing max counter <{}>".format(self.max_counter))
                self.max_counter = self.max_counter - 1
                if self.allmax is None or val > self.allmax:
                    self.allmax = val
                logging.debug("Max counter <{}>".format(self.max_counter))
                if self.all_max_tried:
                    self.allmax_ready.notify_all()

    def print_max(self):
        with self.allmax_ready:
            while not self.all_max_tried:
                self.allmax_ready.wait()
            logging.debug(
                "Printing Max: {}"
                .format(
                    self.allmax
                )
            )


def thread1(expression, val):
    expression.set_max(val)


def thread2(expression, val):
    Z = [0, 1, 2, 3, 4, 5]
    expression.Z = Z
    expression.set_max(val)
    expression.print_max()


def thread3(expression, val):
    expression.set_max(val)


def thread4(expression, val):
    expression.set_max(val)


if __name__ == "__main__":
    expression = Expression(
        d=0,
        MX=0,
        R=0,
        E=0
    )

    t1 = threading.Thread(name="t1", target=thread1, args=(expression, 10,))
    t2 = threading.Thread(name="t2", target=thread2, args=(expression, 1,))
    t3 = threading.Thread(name="t3", target=thread3, args=(expression, 3,))
    t4 = threading.Thread(name="t4", target=thread4, args=(expression, -2,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
