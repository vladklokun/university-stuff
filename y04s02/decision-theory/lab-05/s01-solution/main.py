import payoff_matrix as pm


MACHINE_COSTS = {
    1: (100,  5),
    2: ( 40, 12),
    3: (150,  3),
    4: ( 90,  8),
}


Q_STATES = [1000, 2000, 3000, 4000]


def cost_fn(fixed_cost, cost_per_unit, units):
    return fixed_cost + cost_per_unit * units


def calc_cost_for_alternative(machine, units):
    cost = cost_fn(*machine, units)
    return cost


def get_laplace_alternative(costs_by_machine):
    row_avg = (
        sum(machine_cost_row) / len(machine_cost_row)
        for machine_cost_row in costs_by_machine
    )
    res = max(row_avg)
    return res


def main():
    costs_by_machine = {}
    for machine_name, machine_params in MACHINE_COSTS.items():
        machine_costs = [
            calc_cost_for_alternative(machine_params, q)
            for q in Q_STATES
        ]
        costs_by_machine[machine_name] = machine_costs

    print("Q = {}".format(Q_STATES))

    pm1 = pm.PayoffMatrix(costs_by_machine)
    pm1.print()
    print(
        "Laplace-best alternative: {}".format(pm1.get_laplace_alternative())
    )
    print(
        "Minimax-best alternative: {}".format(pm1.get_minimax_alternative())
    )
    print(
        "Savage-best alternative: {}".format(pm1.get_savage_alternative())
    )
    print(
        "Hurwitz-best alternative: {}".format(pm1.get_hurwitz_alternative())
    )


if __name__ == '__main__':
    main()
