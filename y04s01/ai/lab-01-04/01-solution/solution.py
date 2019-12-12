import argparse
import itertools
import networkx as nx
import matplotlib.pyplot as plt

INF = 9999


class Path(object):

    def __init__(self, path):
        self.path = path

    def __str__(self):
        s = "".join(str(self.path))
        return s

    def __add__(self, other):
        if not isinstance(other, Path):
            raise TypeError(
                "Cannot add {} to Path"
                .format(type(other))
            )

        res = Path(
            self.path + other.path
        )
        return res

    def __hash__(self):
        return hash(self.path)

    def __eq__(self, other):
        return self.path == other.path

    def __len__(self):
        return len(self.path)

    @property
    def name(self):
        name = "".join(self.path)
        return name

    @property
    def subpaths(self):
        for idx in range(1, len(self.path) + 1):
            yield Path(self.path[:idx])

    @property
    def edges(self):
        subpaths = list(self.subpaths)
        src_edge = subpaths[0]
        for dst_edge in subpaths[1:]:
            yield (src_edge, dst_edge)
            src_edge = dst_edge

    def calculate_cost(self, distance_matrix):
        distance = 0
        src_idx = self.path[0]
        for dst_idx in self.path[1:]:
            distance += distance_matrix[src_idx][dst_idx]
            src_idx = dst_idx

        return distance


class SearchTree(nx.Graph):

    SOLUTION_METHODS = {
        "bfs": nx.bfs_tree,
        "dfs": nx.dfs_tree,
    }

    def __init__(self, distance_matrix, *args, **kwargs):

        self.distance_matrix = distance_matrix
        self.shortest_path_length = len(distance_matrix) + 1

        super().__init__(*args, **kwargs)

        self._build()

    def _build(self):
        nodes = list(self.distance_matrix.keys())

        starting_vertex = Path((nodes[0],))
        nodes = nodes[1:]
        for permutation in itertools.permutations(nodes):
            cur_path = starting_vertex + Path(permutation) + starting_vertex
            self.add_path(cur_path)

    def add_path(self, path):
        for sp in path.subpaths:
            self.add_node(sp)

        for src, dst in path.edges:
            self.add_edge(src, dst)

    def show(self, *args, **kwargs):
        nx.draw(self, *args, **kwargs)
        plt.show()

    def solve_tsp(self, starting_v, method="bfs", print_search=False):
        print("Solving using method: {}".format(method))
        try:
            method = self.SOLUTION_METHODS[method]
        except KeyError:
            raise ValueError(
                "I don't know the solution method <{}>"
                .format(method)
            )

        if isinstance(starting_v, str):
            starting_v = Path((starting_v,))

        cur_min = INF

        # Traverse the tree using the selected method
        for n in method(self, starting_v):
            # If the current path length is less than the required minimum,
            # continue the iteration. Used to skip short, unsuitable paths
            if len(n) != self.shortest_path_length:
                continue

            cur_cost = n.calculate_cost(self.distance_matrix)
            if print_search:
                print(
                    "Checking path: {} (Cost: {})"
                    .format(
                        n,
                        cur_cost
                    )
                )
            if cur_cost < cur_min:
                cur_min = cur_cost
                min_path = n

        return min_path


def main(method, print_search=False, *args, **kwargs):
    distances = {
        "A": {"A": INF, "B":   4, "C":   3, "D":   7, "E":   4, "F":   2},
        "B": {"A":   4, "B": INF, "C":   1, "D":   5, "E":   3, "F":   6},
        "C": {"A":   3, "B":   1, "C": INF, "D":   3, "E":   1, "F":   4},
        "D": {"A":   7, "B":   5, "C":   3, "D": INF, "E":   2, "F":   4},
        "E": {"A":   4, "B":   3, "C":   1, "D":   2, "E": INF, "F":   2},
        "F": {"A":   2, "B":   6, "C":   4, "D":   4, "E":   2, "F": INF},
    }

    search_tree = SearchTree(distances)

    minpath = search_tree.solve_tsp(
        starting_v="A",
        method=method,
        print_search=print_search,
    )
    minpathcost = minpath.calculate_cost(distances)

    print(
        "Shortest path: {} ({})"
        .format(
            minpath,
            minpathcost,
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Solve a TSP problem using either DFS or BFS on solution tree."
    )
    parser.add_argument(
        "method",
        type=str,
        default="bfs"
    )
    parser.add_argument(
        "-p",
        "--print-search",
        dest="print_search",
        action="store_true",
        help=(
            "Print the search process."
        )
    )
    parser.set_defaults(print_search=False)

    args = parser.parse_args()
    method = args.method
    print_search = args.print_search
    main(
        method=method,
        print_search=print_search
    )
