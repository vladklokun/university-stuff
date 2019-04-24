#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import multiprocessing as mp
import os
import errno
import itertools as it

import mpp_evaluator.cluster as mppe_c
import mpp_evaluator.topologies as mppe_t
import mpp_evaluator.stats_formatter as mppe_f


def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def calc_scaling_stats(system, cluster, anchor_node, node_count,
                       draw_graphs=False):
    stats = []

    system.anchor_node = anchor_node
    step = 1
    while system.node_count < node_count:
        system.connect_cluster(cluster)
        if draw_graphs:
            system.draw()
        stats.append(
            {
                'step': step,
                'node_count': system.node_count,
                **system.calc_all_params()
            }
        )
        step += 1

    return mppe_f.SystemStats(stats, system.sys_type)


def main(args):
    outdir = args.outdir
    anchor_node = args.anchor_node
    node_count = args.cpus

    c1 = mppe_c.Cluster()
    # c1.from_edgelist(filename=args.edgelist, delimiter='->')
    c1.from_adjlist(filename=args.adjlist, delimiter=', ', nodetype=int)

    line_system = mppe_t.LineSystem()
    ring_system = mppe_t.RingSystem()
    star_system = mppe_t.StarSystem()
    grid_system = mppe_t.GridSystem()

    systems = [line_system, ring_system, star_system, grid_system]
    func_params = [(s, c1, anchor_node, node_count) for s in systems]

    print('Starting calculation. Please, wait.')

    if not args.single_process:
        with mp.Pool(processes=len(func_params)) as pool:
            result = pool.starmap_async(calc_scaling_stats, func_params)
            system_stats = result.get()
    else:
        system_stats = it.starmap(calc_scaling_stats, func_params)

    print('Calculations are done. Printing results.')

    for s in system_stats:
        print('\n# {} System'.format(s.system_type))
        s.print()
        make_sure_path_exists(outdir)
        s.to_csv(outdir + '{}.csv'.format(s.system_type))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'adjlist',
        help='path to adjacency list file'
    )

    parser.add_argument(
        '-n',
        '--anchor_node',
        type=int,
        default=0,
        help=(
            'label of the anchor node -- the node that connects clusters in '
            'a system. Default: 0 (integer zero)'
        )
    )
    parser.add_argument(
        '-c',
        '--cpus',
        type=int,
        default=100,
        help=(
            'target CPU count. Scale a system until this many CPUs are there. '
            'Default: 100'
        )
    )

    parser.add_argument(
        '--outdir',
        default='out/',
        help='path, where the results should be stored. Default: "out/"'
    )

    parser.add_argument(
        '-s',
        '--single_process',
        action='store_true',
        help='run calculations synchronously in a single process.'
    )

    args = parser.parse_args()
    main(args)
