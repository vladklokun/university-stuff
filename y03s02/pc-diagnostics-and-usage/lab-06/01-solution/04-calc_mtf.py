#!/usr/bin/env python3
import argparse
import csv
import math


def main(args):
    lofile = args.lobound_file
    hifile = args.hibound_file

    mtf_points = []
    with open(lofile) as lf, open(hifile) as hf:
        for lorow, hirow in zip(lf, hf):
            if not lorow.startswith('#') and not hirow.startswith('#'):
                print('lr = {}, hr = {}'.format(lorow.split(), hirow.split()))
                x, y_low = map(float, lorow.split())
                _, y_high = map(float, hirow.split())

                r = (y_high - y_low) / (y_high + y_low)
                mtf_points.append((x, r))

    print(mtf_points)

    mtf_file = args.mtf_file
    with open(mtf_file, 'w') as f:
        for x, y in mtf_points:
            f.write('{},{}\n'.format(x, y))
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('lobound_file')
    parser.add_argument('hibound_file')
    parser.add_argument('mtf_file')

    args = parser.parse_args()
    main(args)
