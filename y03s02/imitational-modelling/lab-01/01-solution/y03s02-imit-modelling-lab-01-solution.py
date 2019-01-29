#!/usr/bin/env python3

import random # random.SystemRandom() for generating seed
import math # math.sqrt
import numpy as np

BINS = 11
RANDMIN = 10
RANDMAX = 50

# A class implementing an LCG and relevant methods
class LCG:
    rand_seq = []

    # generator
    def lcg(self, m, a, c, seed):
        while True:
            seed = (a * seed + c) % m
            yield seed

    def __init__(self,
                 m = 0xFFFFFFFE, # modulus M (as per MINSTD)
                 a = 47801, # multiplier a
                 c = 0, # increment c
                 seed = random.SystemRandom().randint(0, 0xFFFFFFFF)):
        self.m, self.a, self.c, self.seed = m, a, c, seed
        self.rand_seq = self.lcg(self.m, self.a, self.c, self.seed)

    def randint(self):
        return next(self.rand_seq)

    def randfloat(self):
        return next(self.rand_seq) / self.m

def calc_freq(seq, a, b):
    cnt = 0
    for x in seq:
        if a < x < b:
            cnt += 1

    return cnt / len(seq)

def calc_mean(seq):
    return sum(seq) / len(seq)

def calc_variance(seq):
    if len(seq) == 1:
        return 0

    mean = calc_mean(seq)
    variance = sum([pow(x - mean, 2) for x in seq]) / len(seq)
    return variance

def calc_stdev(seq):
    return math.sqrt(calc_variance(seq))

def calc_stat_params(seq):
    return calc_mean(seq), calc_variance(seq), calc_stdev(seq)

def calc_chi_squared_pearson(seq):
    m = BINS
    N = len(seq)

    freqs = np.histogram(seq, bins = m)[0] # bin data in m bins

    return m/N * sum([pow( x - N/m, 2) for x in freqs])

def calc_seq_props(seq):
    freq = calc_freq(seq, 0.2113, 0.7887)
    mean = calc_mean(seq)
    variance = calc_variance(seq)
    stdev = calc_stdev(seq)
    chi_squared = calc_chi_squared_pearson(seq)

    return freq, mean, variance, stdev, chi_squared

def calc_all_seq_props(dataset):
    res = []
    for seq in dataset:
        res.append(calc_seq_props(seq))

    return res

def print_res(p):
    print('\n{:-^12} {:-^12} {:-^12} {:-^12} {:-^12}'.format('Freq', 'Mean', 'Variance', 'Stdev', 'chi^2'))
    print()
    for s in p:
        print('{:>12.4f} {:>12.4f} {:>12.4f} {:>12.4f} {:>12.4f}'.format(*s))

def build_rand_range(a, b, count = 10):
    res = []
    for i in range(count):
        res.append(random.randrange(a, b))

    return res


def main():
    lcg = LCG() # instantiate an LCG

    a, b = RANDMIN, RANDMAX # randint bounds

    rand_float_seqs = []
    rand_int_seq = build_rand_range(a, b)

    # build test sequence
    for i in range(10):
        seq = [lcg.randfloat() for x in range(10000)]
        rand_float_seqs.append(seq)

    print('\nTask 1.\nRandom float sequence (first 10 values): {}'.format(rand_float_seqs[0][:10]))

    print('\nTasks 2-3.\nData is separated in {} bins.'.format(BINS))

    properties = calc_all_seq_props(rand_float_seqs)
    print_res(properties)

    print('\nTask 4.\nRandom ({}, {}) sequence: {}'.format(a, b, rand_int_seq))


if __name__ == '__main__':
    main()
