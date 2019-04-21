import argparse
import multiprocessing as mp
import os, errno

import mpp_evaluator.cluster as mppe_c
import mpp_evaluator.topologies as mppe_t
import mpp_evaluator.stats_formatter as mppe_f


def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def calc_scaling_stats(system, cluster, anchor_node, node_count):
    stats = []

    system.anchor_node = anchor_node
    step = 1
    while system.node_count < node_count:
        system.connect_cluster(cluster)
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
    if args.outdir:
        outdir = args.outdir
    else:
        outdir = 'out'

    anchor_node = args.anchor_node
    node_count = args.cpu_count

    c1 = mppe_c.Cluster()
    # c1.from_edgelist(filename=args.edgelist, delimiter='->')
    c1.from_adjlist(filename=args.edgelist, delimiter=', ', nodetype=int)

    line_system = mppe_t.LineSystem()
    ring_system = mppe_t.RingSystem()
    star_system = mppe_t.StarSystem()
    grid_system = mppe_t.GridSystem()

    systems = [line_system, ring_system, star_system, grid_system]
    func_params = [(s, c1, anchor_node, node_count) for s in systems]

    print('Starting calculation. Please, wait.')

    with mp.Pool(processes=len(func_params)) as pool:
        result = pool.starmap_async(calc_scaling_stats, func_params)
        system_stats = result.get()

    for s in system_stats:
        print('\n{}'.format(s.system_type))
        s.print()
        s.to_csv('{}.csv'.format(s.system_type))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('edgelist')
    parser.add_argument('anchor_node', type=int)
    parser.add_argument('cpu_count', type=int)

    parser.add_argument('outdir')

    args = parser.parse_args()
    main(args)
