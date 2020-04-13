GAME_1 = [
    [ 1,  9,  6,  0],
    [ 2,  3,  8,  4],
    [-5, -2, 10, -3],
    [ 7,  4, -2, -5],
]

GAME_2 = [
    [ 1,  9,  6,  8],
    [ 2, 10,  4,  6],
    [-5,  3,  0,  7],
    [ 7, -2,  8,  4],
]

GAME_3 = [
    [ 3,  6,  1],
    [ 5,  2,  3],
    [ 4,  2, -5],
]

GAME_4 = [
    [ 3,  7,  1,  3],
    [ 4,  8,  0, -6],
    [ 6, -9, -2,  4],
]

GAMES = [GAME_1, GAME_2, GAME_3, GAME_4]


def minimax(matrix):
    res = min((
        max(el for el in row)
        for row in matrix
    ))
    return res


def maximin(matrix):
    res = max((
        min(el for el in row)
        for row in matrix
    ))
    return res


def transpose(matrix):
    res = list(map(list, zip(*matrix)))
    return res


def calc_rowmin(matrix):
    return maximin(matrix)


def calc_colmax(matrix):
    return minimax(transpose(matrix))


def main():
    for g in GAMES:
        lower_bound = calc_rowmin(g)
        upper_bound = calc_colmax(g)
        print("Range: ({}, {})".format(lower_bound, upper_bound))


if __name__ == '__main__':
    main()
