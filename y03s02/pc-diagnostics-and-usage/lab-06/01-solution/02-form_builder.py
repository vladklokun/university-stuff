#!/usr/bin/env python3
import argparse
import csv
import math


class Measurement(object):
    def __init__(self, num, x, y, r, g, b, i, h, s, v):
        self.num = float(num)
        self.x = float(x)
        self.y = float(y)
        self.r = float(r)
        self.g = float(g)
        self.b = float(b)
        self.i = float(i)
        self.h = float(h)
        self.s = float(s)
        self.v = float(v)
        self.frequency = None

    def __str__(self):
        s = (
            '<Point: num="{}" x = "{}" y = "{}" r = "{}" g = "{}" b = "{}" '
            'i = "{}", h = "{}", s = "{}", v = "{}">'
        ).format(
            self.num, self.x, self.y, self.r, self.g, self.b,
            self.i, self.h, self.s, self.v
        )
        return s


def main(args):
    infile = args.infile
    with open(infile) as csvfile:
        reader = csv.reader(row for row in csvfile if not row.startswith('#'))
        points = [Measurement(*row) for row in reader]

    for p in points:
        print(p)

    last_p = max([p.num for p in points])
    print('last_p = {}'.format(last_p))

    # Find min and max point value for frequency computation
    p_vals = [p.v for p in points]
    # Set min to 2 to avoid float division by zero and log domain error
    f_min = 2
    f_max = max(p_vals)

    # Calculate frequencies for each point
    for p in points:
        print(
            'num = {}, last_p = {}, f_max = {}, f_min = {}'
            .format(p.num, last_p, math.log(f_max), math.log(f_min))
        )
        res = 2 * math.exp(p.num/last_p * (math.log(f_max) / math.log(f_min)))
        p.frequency = res
        print('p.frequency = {}'.format(p.frequency))

    freq_plot = [(p.num, p.i) for p in points]
    with open(args.freq_intensity_file, 'w') as outfile:
        for frequency, intensity in freq_plot:
            outfile.write('{},{}\n'.format(frequency, intensity))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    parser.add_argument('freq_intensity_file')

    args = parser.parse_args()
    main(args)
