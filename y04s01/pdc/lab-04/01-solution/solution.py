import copy
import functools
import threading
import logging
import random

import numpy as np

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(threadName)s: %(message)s",
)


THREAD_COUNT = 4

DIMENSION = 5
Z_INIT_VALS = [6, 3, 2, 8, 11]

R_FILL = 2
E_FILL = 3
MX_FILL = 4


def synchronized(wrapped):
    """Decorator that wraps the function to make it thread-safe: it can only be
    executed by one thread at a time.
    """
    lock = threading.Lock()
    @functools.wraps(wrapped)
    def _wrap(*args, **kwargs):
        with lock:
            return wrapped(*args, **kwargs)

    return _wrap


def eval_A_h(A, maxall, R, d, E, MX, start, stop, dim=DIMENSION):
    """Evaluates a part of `A` given the passed parameters.

    Args:
        A: the object where the result will be written
        maxall: the maxall value
        R: the value of vector R
        E: the value of vector E
        MX: the value of matrix MX
        start: starting index
        stop: stopping index
        dim (default: DIMENSION): element dimensions
    """
    R_H = R[start:stop]
    MX_H = MX[:, start:stop]
    A[start:stop] = maxall * R_H + d * (E.dot(MX_H))


class Expression(object):

    def __init__(self, *args, **kwargs):
        # Inner, protected shared resources
        self._d = None
        self.d_cv = threading.Condition()
        self.d_input = False

        self._E = None
        self.E_cv = threading.Condition()
        self.E_input = False

        self._maxall = None
        self.maxall_cv = threading.Condition()
        self.maxall_finalized = False

        self.max_counter = DIMENSION
        self.max_counter_cv = threading.Condition()

        # Signals for outer resources
        self.Z_cv = threading.Condition()
        self.Z_input = False

        self.MX_cv = threading.Condition()
        self.MX_input = False

        self.R_cv = threading.Condition()
        self.R_input = False

        self.A_cv = threading.Condition()
        self.A_h_counter = THREAD_COUNT

    @property
    def all_max_tried(self):
        return self.max_counter == 0

    @property
    @synchronized
    def maxall(self):
        return self._maxall

    @property
    @synchronized
    def d(self):
        return self._d

    @d.setter
    @synchronized
    def d(self, val):
        with self.d_cv:
            self._d = val
            self.d_input = True
            self.d_cv.notify_all()

    @property
    @synchronized
    def E(self):
        return self._E.copy()

    @E.setter
    @synchronized
    def E(self, val):
        self._E = val

    @synchronized
    def set_max(self, vec):
        """Sets max value"""
        with self.maxall_cv:
            for candidate_val in vec:
                if self._maxall is None or candidate_val > self._maxall:
                    self._maxall = candidate_val
            self.max_counter = self.max_counter - len(vec)

            if self.all_max_tried:
                self.maxall_finalized = True
                self.maxall_cv.notify_all()

    def print_max(self):
        with self.maxall_cv:
            while not self.maxall_finalized:
                self.maxall_cv.wait()

    @synchronized
    def thread_finished_A_h(self):
        self.A_h_counter -= 1
        if self.A_h_counter == 0:
            with self.A_cv:
                self.A_cv.notify_all()

    @property
    @synchronized
    def A_finalized(self):
        return self.A_h_counter == 0

    def wait_maxall_finalized(self):
        with self.maxall_cv:
            while not self.maxall_finalized:
                self.maxall_cv.wait()
            return

    def signal_maxall_finalized(self):
        with self.maxall_cv:
            self.maxall_finalized = True
            self.maxall_cv.notify_all()

    def wait_Z_input(self):
        with self.Z_cv:
            while not self.Z_input:
                self.Z_cv.wait()
            return

    def signal_Z_input(self):
        with self.Z_cv:
            self.Z_input = True
            self.Z_cv.notify_all()

    def wait_d_input(self):
        with self.d_cv:
            while not self.d_input:
                self.d_cv.wait()
            return

    def signal_d_input(self):
        with self.d_cv:
            self.d_input = True
            self.d_cv.notify_all()

    def wait_MX_input(self):
        with self.MX_cv:
            while not self.MX_input:
                self.MX_cv.wait()
            return

    def signal_MX_input(self):
        with self.MX_cv:
            self.MX_input = True
            self.MX_cv.notify_all()

    def wait_R_input(self):
        with self.R_cv:
            while not self.R_input:
                self.R_cv.wait()
            return

    def signal_R_input(self):
        with self.R_cv:
            self.R_input = True
            self.R_cv.notify_all()

    def wait_E_input(self):
        with self.E_cv:
            while not self.E_input:
                self.E_cv.wait()
            return

    def signal_E_input(self):
        with self.E_cv:
            self.E_input = True
            self.E_cv.notify_all()

    def wait_A_finished(self):
        with self.A_cv:
            while not self.A_finalized:
                self.A_cv.wait()
            return

    def signal_A_finished(self):
        with self.A_cv:
            self.A_finalized = True
            self.A_cv.notify_all()


def thread1(expression, A, Z, R, E, d, MX):
    expression.wait_Z_input()
    expression.set_max(Z[0:1])

    expression.wait_maxall_finalized()

    maxall1 = expression.maxall

    expression.wait_d_input()
    d1 = expression.d

    expression.wait_E_input()
    E1 = expression.E

    eval_A_h(A, maxall1, R, d1, E1, MX, 0, 1)
    expression.thread_finished_A_h()



def thread2(expression, A, Z, R, E, d, MX):
    with expression.Z_cv:
        # Initialize Z
        for idx, val in enumerate(Z_INIT_VALS):
            Z[idx] = val
        # Notify subscribers
        expression.Z_input = True
        expression.Z_cv.notify_all()

    expression.set_max(Z[1:2])

    expression.wait_maxall_finalized()
    maxall2 = expression.maxall

    with expression.d_cv:
        while not expression.d_input:
            expression.d_cv.wait()
        d2 = expression.d

    with expression.MX_cv:
        while not expression.MX_input:
            expression.MX_cv.wait()

    with expression.E_cv:
        while not expression.E_input:
            expression.MX_cv.wait()
        E2 = expression.E

    with expression.R_cv:
        while not expression.R_input:
            expression.R_cv.wait()
    # Evaluate the thread's part
    eval_A_h(A, maxall2, R, d2, E2, MX, 1, 2)
    expression.thread_finished_A_h()

    # Wait for A to finish
    expression.wait_A_finished()
    print("A = {}".format(A))


def thread3(expression, A, Z, R, E, d, MX):
    # Initialize R
    with expression.R_cv:
        R.fill(R_FILL)
        expression.R_input = True
        expression.R_cv.notify_all()

    # Initialize E
    with expression.E_cv:
        expression.E = np.full(DIMENSION, E_FILL)
        E = expression.E
        expression.E_input = True
        expression.E_cv.notify_all()


    with expression.Z_cv:
        while not expression.Z_input:
            expression.Z_cv.wait()

        expression.set_max(Z[2:3])

    expression.wait_maxall_finalized()
    maxall3 = expression.maxall

    expression.wait_d_input()
    d3 = expression.d

    expression.wait_MX_input()

    # Evaluate the thread's part
    eval_A_h(A, maxall3, R, d3, E, MX, 2, 3)
    expression.thread_finished_A_h()


def thread4(expression, A, Z, R, E, d, MX):
    # Input d
    d = 5
    expression.d = d

    with expression.MX_cv:
        # Input MX
        MX.fill(MX_FILL)
        # Notify subscribers
        expression.MX_input = True
        expression.MX_cv.notify_all()

    expression.wait_Z_input()
    expression.set_max(Z[3:5])

    maxall4 = expression.maxall

    expression.wait_R_input()
    expression.wait_E_input()
    E4 = expression.E

    # Evaluate the thread's part
    eval_A_h(A, maxall4, R, d, E4, MX, 3, 5)
    expression.thread_finished_A_h()


if __name__ == "__main__":
    expression = Expression(
        d=0,
        MX=0,
        R=0,
        E=0
    )

    A = np.ndarray(DIMENSION, np.int32)
    R = np.ndarray(DIMENSION, np.int32)
    E = np.ndarray(DIMENSION, np.int32)
    Z = np.ndarray(DIMENSION, np.int32)
    d = 0
    MX = np.zeros((DIMENSION, DIMENSION))

    t1 = threading.Thread(
        name="t1",
        target=thread1,
        kwargs={
            "expression": expression,
            "A": A,
            "Z": Z,
            "R": R,
            "E": E,
            "d": d,
            "MX": MX,
        }
    )

    t2 = threading.Thread(
        name="t2",
        target=thread2,
        kwargs={
            "expression": expression,
            "A": A,
            "Z": Z,
            "R": R,
            "E": E,
            "d": d,
            "MX": MX,
        }
    )

    t3 = threading.Thread(
        name="t3",
        target=thread3,
        kwargs={
            "expression": expression,
            "A": A,
            "Z": Z,
            "R": R,
            "E": E,
            "d": d,
            "MX": MX,
        }
    )

    t4 = threading.Thread(
        name="t4",
        target=thread4,
        kwargs={
            "expression": expression,
            "A": A,
            "Z": Z,
            "R": R,
            "E": E,
            "d": d,
            "MX": MX,
        }
    )

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
