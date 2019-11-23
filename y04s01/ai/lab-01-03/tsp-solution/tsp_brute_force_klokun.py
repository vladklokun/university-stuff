import itertools

INF = 9999

def gen_route_chain(permutation):
    route = []
    src_idx = permutation[0]
    for node_idx in permutation[1:]:
        dst_idx = node_idx
        route.append((src_idx, dst_idx))
        src_idx = dst_idx

    return route


def calc_distance(route, distance_matrix):
    distance = 0
    src_idx = route[0]
    for dst_idx in route[1:]:
        distance += distance_matrix[src_idx][dst_idx]
        src_idx = dst_idx

    return distance

def main():
    distances = {
        "A": {"A":  INF, "B":    4, "C":    3, "D":    7, "E":    4, "F":    2},
        "B": {"A":    4, "B":  INF, "C":    1, "D":    5, "E":    3, "F":    6},
        "C": {"A":    3, "B":    1, "C":  INF, "D":    3, "E":    1, "F":    4},
        "D": {"A":    7, "B":    5, "C":    3, "D":  INF, "E":    2, "F":    4},
        "E": {"A":    4, "B":    3, "C":    1, "D":    2, "E":  INF, "F":    2},
        "F": {"A":    2, "B":    6, "C":    4, "D":    4, "E":    2, "F":  INF},
    }
    nodes = {**distances}
    nodes.pop("A")
    nodes = nodes.keys()

    distance_min = INF
    for permutation in itertools.permutations(nodes):
        # Always start at node "1"
        route_cur = ("A", ) + permutation + ("A",)

        distance_cur = calc_distance(route_cur, distances)
        print(
            "Route: {} Distance {}"
            .format(route_cur, distance_cur)
        )
        if distance_cur < distance_min:
            distance_min = distance_cur
            route_min = route_cur

    print(
        "Route_min: {} Distance_min: {}"
        .format(route_min, distance_min)
    )

if __name__ == "__main__":
    main()
