import matplotlib.pyplot as plt
import numpy as np


GAME_1 = [
    [  1, -3,  7],
    [  2,  4, -6],
]


GAME_2 = [
    [  5,  8],
    [  6,  5],
    [  5,  7],
]

GAMES = [GAME_1, GAME_2]


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def build_coefficients_from_game(game):
    coeffs = []

    game_transposed = transpose(game)

    for row in game_transposed:
        new_row = [row[0] - row[1], row[1]]
        coeffs.append(list(reversed(new_row)))

    return coeffs


def calc_fn_by_coefficients(coeffictients, x):
    """Calculates the value of a polynomial function f(x) by its coefficients.
    """
    res = 0
    for idx, c in enumerate(coeffictients):
        res += (c * x**idx)

    return res


def main():
    x = np.arange(0, 1, 0.1)
    fig, axs = plt.subplots(2, 1)
    ax1, ax2 = axs

    coeffs = build_coefficients_from_game(GAME_1)
    print(coeffs)
    ax1.set_title("Game 1")
    for idx, c in enumerate(coeffs, start=1):
        ax1.plot(
            x,
            [calc_fn_by_coefficients(c, i) for i in x],
            label="B{}".format(idx)
        )

    plt.tight_layout()

    coeffs = build_coefficients_from_game(transpose(GAME_2))
    print(coeffs)
    ax2.set_title("Game 2")
    for idx, c in enumerate(coeffs, start=1):
        ax2.plot(
            x,
            [calc_fn_by_coefficients(c, i) for i in x],
            label="A{}".format(idx)
        )

    ax1.legend()
    ax2.legend()
    plt.show()


if __name__ == '__main__':
    main()
