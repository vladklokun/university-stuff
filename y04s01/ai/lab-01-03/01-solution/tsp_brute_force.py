import itertools

INFTY = 1000000

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
        "1": {"1": 9999, "2":    9, "3":    7, "4": 9999, "5": 9999, "6":    5},
        "2": {"1":    9, "2": 9999, "3":    5, "4":    9, "5":   10, "6":    8},
        "3": {"1":    7, "2":    5, "3": 9999, "4":    5, "5": 9999, "6":    3},
        "4": {"1": 9999, "2":    9, "3":    5, "4": 9999, "5":    4, "6":    6},
        "5": {"1":    9, "2":   10, "3": 9999, "4":    4, "5": 9999, "6":    5},
        "6": {"1":    5, "2":    8, "3":    3, "4":    6, "5":    5, "6": 9999},
    }
    nodes = distances.keys()

    print(nodes)

    distance_min = INFTY
    for permutation in itertools.permutations(nodes):
        # Always start at node "1"
        route_cur = ("1", ) + permutation

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
