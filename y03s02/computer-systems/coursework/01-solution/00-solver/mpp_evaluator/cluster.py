#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np  # for compatibility with to_numpy_matrix()
import networkx as nx


class Cluster(object):
    """ Describes a computing cluster """
    def __init__(self, graph=None):
        self._graph = nx.Graph()

    def __str__(self):
        s = self.get_adjacency_matrix()
        return str(s)

    @property
    def graph(self):
        """ Get the current Cluster graph """
        return self._graph

    @graph.setter
    def graph(self, new_graph):
        """ Set the current Cluster graph to a Graph object """
        self._graph = new_graph

    def get_adjacency_matrix(self):
        """ Get a NumPy adjacency matrix from Cluster's Graph object """
        return nx.to_numpy_matrix(self.graph)

    def add_connection(self, src, dest):
        self.graph.add_edge(src, dest)

    def from_edgelist(self, filename, delimiter=None, nodetype=int):
        """ Loads a Cluster from its edge list stored in a file `filename`
        """
        with open(filename, 'r') as f:
            self.graph = nx.parse_edgelist(
                lines=f,
                nodetype=nodetype,
                delimiter=delimiter
            )

    def from_adjlist(self, filename, delimiter=None, nodetype=int):
        """ Loads a Cluster from its adjacency list stored in a file `filename`
        """
        with open(filename, 'r') as f:
            graph = nx.parse_adjlist(
                lines=f,
                nodetype=nodetype,
                delimiter=delimiter
            )

        self.graph = graph
