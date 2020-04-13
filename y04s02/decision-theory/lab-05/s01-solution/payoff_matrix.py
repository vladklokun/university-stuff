class PayoffMatrix(object):

    def __init__(self, matrix, opt_fn=min, not_opt_fn=max):
        self._raw_matrix = matrix
        self.matrix = self.parse_raw_matrix(matrix)
        self.opt_fn = opt_fn
        self.not_opt_fn = min if opt_fn is max else max

    @property
    def rows(self):
        for row in self._raw_matrix.items():
            yield row

    @staticmethod
    def parse_raw_matrix(raw_matrix):
        parsed = [row for row in raw_matrix.values()]
        return parsed

    def print(self):
        print("Payoff Matrix")
        for machine, params in self._raw_matrix.items():
            print(
                "Machine {}: {}"
                .format(machine, params)
            )

    @staticmethod
    def laplace_key(row):
        """Key function for finding the Laplace criterion favourite."""
        _, params = row
        return sum(params) / len(params)

    def get_laplace_alternative(self):
        res = self.opt_fn(self.rows, key=self.laplace_key)
        return res

    def minimax_key(self, row):
        """Key function for finding the minimax (maximin) criterion favourite.
        """
        _, params = row
        return self.not_opt_fn(params)

    def get_minimax_alternative(self):
        res = self.opt_fn(self.rows, key=self.minimax_key)
        return res

    @staticmethod
    def transpose(matrix):
        return list(map(list, zip(*matrix)))

    def calc_regret_matrix(self):
        col_opts = [self.opt_fn(row) for row in self.transpose(self.matrix)]

        regret_matrix = {}
        for machine, params in self.rows:
            regret_row = []
            for el, col_opt in zip(params, col_opts):
                regret_row.append(el - col_opt)
            regret_matrix[machine] = regret_row

        res = PayoffMatrix(regret_matrix, opt_fn=max)
        return res

    def get_savage_alternative(self):
        regret_matrix = self.calc_regret_matrix()
        machine, params = regret_matrix.get_minimax_alternative()
        res = self._raw_matrix[machine]
        return (machine, res)

    def hurwitz_key(self, row):
        """Key function for finding the Hurwitz criterion favourite."""
        _, params = row
        left_term = self.hurwitz_alpha * self.opt_fn(params)
        right_term = (1 - self.hurwitz_alpha) * self.not_opt_fn(params)
        return left_term + right_term

    def get_hurwitz_alternative(self, alpha=0.5):

        def hurwitz_key(row):
            """Inner key function for finding the best alternative
            according to the Hurwitz criterion.

            Used to account for variable alpha parameter.
            """
            _, params = row
            left_term = alpha * self.opt_fn(params)
            right_term = (1 - alpha) * self.not_opt_fn(params)
            return left_term + right_term

        res = self.opt_fn(self.rows, key=hurwitz_key)
        return res
