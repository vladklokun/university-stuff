import copy

import networkx as nx  # graph operations
import numpy as np  # compatibility with to_numpy_matrix()

import matplotlib.pyplot as plt


class System(object):
    """ Describes a generic Massively Parallel Processing System """
    def __init__(self, clusters=None):
        self._clusters = None
        if clusters:
            self.clusters = clusters
        else:
            self.clusters = []

        self.intercluster_conn = []

        self._node_count = 0
        self._anchor_node = None

        self._update_graph()

    def __str__(self):
        s = str(nx.to_numpy_matrix(self.graph))
        return s

    @property
    def clusters(self):
        return self._clusters

    @clusters.setter
    def clusters(self, new_clusters):
        self._clusters = new_clusters

    @property
    def graph(self):
        return self._graph

    @graph.setter
    def graph(self, new_graph):
        self._graph = new_graph

    @property
    def node_count(self):
        return self._node_count

    @node_count.setter
    def node_count(self, new_node_count):
        self._node_count = new_node_count

    @property
    def anchor_node(self):
        return self._anchor_node

    @anchor_node.setter
    def anchor_node(self, new_anchor_node):
        self._anchor_node = new_anchor_node

    def add_cluster(self, cluster):
        # Make an independent copy of a passed cluster
        tmp_cluster = copy.deepcopy(cluster)

        # Rename nodes in copied cluster
        prefix = len(self.clusters)
        self._relabel_cluster_nodes(tmp_cluster, prefix)
        self.clusters.append(tmp_cluster)

        # Update Topology graph
        self._update_graph()

        # Update CPU number
        self.node_count = len(self.graph.nodes())

    @staticmethod
    def _relabel_cluster_nodes(cluster, graph_prefix):
        relabel_mapping = {
            node_name: (graph_prefix, node_name)
            for node_name in cluster.graph.nodes()
        }

        # Relabel nodes in place
        nx.relabel_nodes(cluster.graph, relabel_mapping, copy=False)

    def _update_graph(self):
        graph = nx.Graph()

        # Add clusters to graph
        for c in self.clusters:
            graph = nx.union(graph, c.graph)

        # Add conection edges
        for conn in self.intercluster_conn:
            graph.add_edge(*conn)

        self.graph = graph

    def connect_nodes(self, src, dest):
        edge = (src, dest)
        self.intercluster_conn.append(edge)
        self.graph.add_edge(*edge)

    def disconnect_nodes(self, src, dest):
        edge = (src, dest)
        self.intercluster_conn.remove(edge)
        self.graph.remove_edge(*edge)

    def calc_diameter(self):
        return nx.diameter(self.graph)

    def calc_avg_diameter(self):
        """ Calculate the system's average diameter

        Average diameter is defined as a sum of diameters divided by number of
        CPUs
        """
        # Shortest path lengths per node
        spath_lengths_per_node = nx.all_pairs_shortest_path_length(self.graph)

        d_sum = 0
        # Ignore the node and access only its shortest path lengths
        for _, spath_lengths in spath_lengths_per_node:
            # Slice a list from the 1st element, since the 1st element is the
            # shortest path length to the node itself, and average diameter
            # disregards this
            lengths = list(spath_lengths.values())
            d_sum += sum(lengths)

        avg_diameter = d_sum / (self.node_count * (self.node_count - 1))

        return avg_diameter

    def calc_degree(self):
        """ Calculates the degree of the system

        Degree of the system is defined as the maximum degree of its graph
        """
        degrees = [degree for node, degree in self.graph.degree()]
        sys_degree = max(degrees)

        return sys_degree

    def calc_cost(self):
        """ Calculates the cost of the system

        Cost of the system is defined as a quanity of edges
        """
        cost = len(self.graph.edges())
        return cost

    def calc_traffic(self):
        """ Calculates the traffic of a system """
        traffic = 2*self.calc_avg_diameter() / self.calc_degree()

        return traffic

    def calc_all_params(self):
        sys_params = {
            'diameter': self.calc_diameter(),
            'avg_diameter': self.calc_avg_diameter(),
            'degree': self.calc_degree(),
            'cost': self.calc_cost(),
            'traffic': self.calc_traffic()
        }

        return sys_params

    def draw(self):
        """ Draws a graph representation of a system """
        nx.draw_circular(self.graph, with_labels=True)
        plt.show()


class LineSystem(System):
    sys_type = 'Line'
    """ A system with Line topology """
    def connect_cluster(self, cluster, src_node_label=None,
                        dest_node_label=None):
        """ Adds and connects a cluster to the existing system """
        self.add_cluster(cluster)

        # Determine connection points
        if src_node_label is None and dest_node_label is None:
            src_node_label = self.anchor_node
            dest_node_label = self.anchor_node

        # Connect clusters
        cluster_count = len(self.clusters)
        # We can only connect more than 1 cluster
        if cluster_count > 1:
            self.connect_nodes(
                src=(cluster_count-2, src_node_label),
                dest=(cluster_count-1, dest_node_label)
            )


class RingSystem(System):
    """ A system with Ring topology """

    sys_type = 'Ring'

    def connect_cluster(self, cluster, src_node_label=None,
                        dest_node_label=None):
        """ Adds and connects a cluster to the existing system """
        self.remove_loop()
        self.add_cluster(cluster)

        # Use pre-set anchors as default connection points
        if src_node_label is None and dest_node_label is None:
            src_node_label = self.anchor_node
            dest_node_label = self.anchor_node

        # Connect clusters
        cluster_count = len(self.clusters)
        # We can only connect more than 1 cluster
        if cluster_count > 1:
            self.connect_nodes(
                src=(cluster_count-2, src_node_label),
                dest=(cluster_count-1, dest_node_label)
            )

        self.add_loop()

    def get_possible_loop(self):
        """ Get an edge that describes a possible loop in RingSystem """
        # Get a set of cluster numbers
        clusters = {cluster_no for cluster_no, _ in self.graph.nodes}

        # No loops are possible in less than 3 clusters
        if len(clusters) < 3:
            return None

        min_cluster = min(clusters)
        max_cluster = max(clusters)

        min_cluster_anchor = (min_cluster, self.anchor_node)
        max_cluster_anchor = (max_cluster, self.anchor_node)

        loop = (min_cluster_anchor, max_cluster_anchor)
        return loop

    def get_loop(self):
        loop = self.get_possible_loop()
        if loop is not None and self.graph.has_edge(*loop):
            return loop

        return None

    def add_loop(self):
        """ Adds a loop in the Ring

        A loop is always between the nodes of the first and the last cluster
        """
        pos_loop = self.get_possible_loop()
        if pos_loop is not None:
            self.connect_nodes(*pos_loop)

    def remove_loop(self):
        if self.get_loop() is not None:
            self.disconnect_nodes(*self.get_loop())


class StarSystem(System):

    sys_type = 'Star'

    def connect_cluster(self, cluster, src_node_label=None,
                        dest_node_label=None):
        """ Adds and connects a cluster to the existing system """
        self.add_cluster(cluster)

        # Determine connection points
        if src_node_label is None and dest_node_label is None:
            src_node_label = self.anchor_node
            dest_node_label = self.anchor_node

        # Connect clusters
        cluster_count = len(self.clusters)
        # We can only connect more than 1 cluster
        if cluster_count > 1:
            self.connect_nodes(
                # 0 means we grow on the 1st (base) cluster
                src=(0, src_node_label),
                dest=(cluster_count-1, dest_node_label)
            )


class GridSystem(System):
    """ """

    sys_type = 'Grid'
    # Source cluster: connect_to cluster
    # E.g: for record "7: (6, 3)" connections to be made:
    # 7 -> 6
    # 7 -> 3
    grid_growth_lut = {
        0: (None, None),
        1: (0, None),
        2: (None, 0),
        3: (2, 1),
        4: (1, None),
        5: (3, 4),
        6: (None, 2),
        7: (6, 3),
        8: (7, 5),
        9: (4, None),
        10: (5, 9),
        11: (8, 10),
        12: (None, 6),
        13: (12, 7),
        14: (13, 8),
        15: (14, 11),
        16: (9, None),
        17: (10, 16),
        18: (11, 17),
        19: (15, 18),
        20: (None, 12),
        21: (20, 13),
        22: (21, 14),
        23: (22, 15),
        24: (23, 19),
    }

    def connect_cluster(self, cluster, src_node_label=None,
                        dest_node_label=None):
        """ Adds and connects a cluster to the existing system """
        self.add_cluster(cluster)

        # Determine connection points
        if src_node_label is None and dest_node_label is None:
            src_node_label = self.anchor_node
            dest_node_label = self.anchor_node

        # Connect clusters
        cluster_count = len(self.clusters)
        # We can only connect more than 1 cluster
        if cluster_count > 1:
            cluster_nos = self._get_connective_cluster_nos()
            for c_no in cluster_nos:
                if c_no is not None:
                    self.connect_nodes(
                        src=(cluster_count-1, src_node_label),
                        dest=(c_no, dest_node_label)
                    )

    def _get_connective_cluster_nos(self):
        cluster_index = len(self.clusters)-1
        try:
            connective_clusters = self.grid_growth_lut[cluster_index]
        except KeyError:
            raise ValueError(
                'No look-up values for value {} in Grid look-up table'
            )

        return connective_clusters
