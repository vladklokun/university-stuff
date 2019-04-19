import argparse
import mpp_evaluator.cluster as mppe_c
import mpp_evaluator.topologies as mppe_t


def main(args):
    c1 = mppe_c.Cluster()
    # c1.from_edgelist(filename=args.edgelist, delimiter='->')
    c1.from_adjlist(filename=args.edgelist, delimiter=', ', nodetype=int)

    line_system = mppe_t.LineSystem()
    line_system.anchor_node = 4  # set the node number on which we should scale
    node_count = 64
    while line_system.node_count < node_count:
        line_system.connect_cluster(
            cluster=c1
        )
        print('Line System Params = {}'.format(line_system.calc_all_params()))

    ring_system = mppe_t.RingSystem()
    ring_system.anchor_node = 4
    node_count = 64
    while ring_system.node_count < node_count:
        ring_system.connect_cluster(
            cluster=c1
        )
        print('Ring System Params = {}'.format(ring_system.calc_all_params()))

    star_system = mppe_t.StarSystem()
    star_system.anchor_node = 4
    node_count = 64
    while star_system.node_count < node_count:
        star_system.connect_cluster(
            cluster=c1
        )
        print('Star System Params = {}'.format(star_system.calc_all_params()))
        # star_system.draw()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('edgelist')

    args = parser.parse_args()
    main(args)
