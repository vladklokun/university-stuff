# -*- coding: utf-8 -*-
import argparse
import datetime

import numpy as np
import pandas as pd
import tabulate


class ProbabilityMatrix(object):
    def __init__(self, fp_pm, fp_ck, fp_cl, fp_fmap):
        self.prob_matrix = self.load_pm(fp_pm)
        self.coeffs_k = self.load_ck(fp_ck)
        self.coeffs_l = self.load_cl(fp_cl)
        self.file_vertice_map = self.load_fvmap(fp_fmap)

        self.eq_system = self.build_eq_system()
        self.n_vals_all = self.solve_eq_system()
        self.n_vals_op = self.get_n_vals_op()
        self.n_vals_io = self.get_n_vals_io()
        self.theta_primary = self.calc_theta_primary()
        self.avg_calls_all_files = self.calc_avg_calls_all_files()
        self.avg_infocount_all_files = self.calc_avg_infocount_all_files()
        self.theta_0 = self.calc_theta_0()

    def load_pm(self, fp_pm):
        probability_matrix = np.loadtxt(fp_pm)
        if args.p:
            print('pm = {}'.format(probability_matrix))
        return probability_matrix

    def load_ck(self, fp_ck):
        coeffs_k = np.loadtxt(fp_ck)
        if args.p:
            print('ck = {}'.format(coeffs_k))
        return coeffs_k

    def load_cl(self, fp_cl):
        coeffs_l = np.loadtxt(fp_cl)
        if args.p:
            print('cl = {}'.format(coeffs_l))
        return coeffs_l

    def load_fvmap(self, fp_fmap):
        d = {}
        for idx, line in enumerate(fp_fmap):
            if not line.startswith('#'):
                d[idx] = [int(x) for x in line.strip().split()]

        if args.p:
            print('d = {}'.format(d))
        return d

    def build_eq_system(self):
        m = self.prob_matrix  # load probability matrix
        if args.p:
            print('m = {}'.format(m))

        m_t = m.transpose()
        if args.p:
            print('m_t = {}'.format(m_t))

        np.fill_diagonal(m_t, -1)  # fill diagonal with '-1'
        if args.p:
            print('m_t_filled = {}'.format(m_t))

        # Create right hand side vector
        # First value is always -1, every other is 0
        rhs = [-1]
        for i in range(len(m_t) - 1):
            rhs.append(0.0)

        return m_t, rhs

    def solve_eq_system(self):
        matrix, rhs = self.eq_system
        x = np.linalg.solve(matrix, rhs)  # since eq_sys is a tuple, unpack it

        if args.p:
            print('x = {}'.format(x))
        return x

    """ This function returns n_vals for operator vertices
    Every second n_val is n_val_operator, so return it
    """
    def get_n_vals_op(self):
        if args.p:
            print('n_vals_op = {}'.format(self.n_vals_all[::2]))
        return self.n_vals_all[::2]

    """ This function returns n_vals for io vertices
    Every second n_val starting from 2nd is n_val_io, so return it
    """
    def get_n_vals_io(self):
        if args.p:
            print('n_vals_io = {}'.format(self.n_vals_all[1::2]))
        return self.n_vals_all[1::2]

    def calc_theta_primary(self):
        theta_primary = 0
        for n_val, coef_k in zip(self.get_n_vals_op(), self.coeffs_k):
            if args.p:
                print('n_val = {}, coef_k = {}'.format(n_val, coef_k))
            theta_primary += n_val * coef_k

        if args.p:
            print('theta_primary = {}'.format(theta_primary))
        return theta_primary

    def calc_avg_calls_per_file(self, vertice_list):
        if args.p:
            print(vertice_list)
        file_n_vals = [self.n_vals_io[i-1] for i in vertice_list]

        if args.p:
            print('file_n_vals = {}'.format(file_n_vals))

        return sum(file_n_vals)

    def calc_avg_calls_all_files(self):
        d = {}
        for idx, vertice_list in enumerate(self.file_vertice_map.values()):
            if args.p:
                print(idx, vertice_list)
            d[idx] = self.calc_avg_calls_per_file(vertice_list)
            if args.p:
                print(d[idx])
        return d

    def calc_avg_infocount_per_file(self, vertice_list):
        file_probs = [self.n_vals_io[i-1] for i in vertice_list]
        if args.p:
            print('file_probs = {}'.format(file_probs))

        file_info_count = [self.coeffs_l[i-1] for i in vertice_list]
        if args.p:
            print('file_info_count = {}'.format(file_info_count))

        N_h = self.calc_avg_calls_per_file(vertice_list)
        a = 1 / N_h
        b = sum([n_i * l_i for n_i, l_i in zip(file_probs, file_info_count)])
        if args.p:
            print('b = {}'.format(b))
        res = a * b
        if args.p:
            print('avg_infocount_per_file = {}'.format(res))
        return res

    def calc_avg_infocount_all_files(self):
        d = {}
        for idx, vertice_list in enumerate(self.file_vertice_map.values()):
            if args.p:
                print(idx, vertice_list)
            d[idx] = self.calc_avg_infocount_per_file(vertice_list)
            if args.p:
                print(d[idx])
        return d

    def calc_theta_0(self):
        N = sum(self.n_vals_op)
        if args.p:
            print('N = {}'.format(N))
        theta_0 = self.theta_primary / N
        if args.p:
            print('theta_0 = {}'.format(theta_0))
        return theta_0

    def dump_eq_sys_coeffs(self, filename):
        eq_system_coeffs, eq_system_rhs = self.eq_system

        # Since we need to concatenate RHS to a 2-D matrix,
        # we create an NP Array from 1-D list and wrap it in another list
        # to make it a 1-column matrix (vertical vector)
        eq_system_rhs = np.array([eq_system_rhs])
        col_names = [
            'n_{a1}', 'n_{b1}',
            'n_{a2}', 'n_{b2}',
            'n_{a3}', 'n_{b3}',
            'n_{a4}', 'n_{b4}',
            'n_{a5}', 'n_{b5}',
            'n_{a6}', 'n_{b6}',
            'n_{a7}', 'n_{b7}',
            'n_{a8}', 'n_{b8}',
            '= x'
        ]
        d = np.concatenate((eq_system_coeffs, eq_system_rhs.T), axis=1)
        df = pd.DataFrame(
            data=d,
            columns=col_names
        )
        s = tabulate.tabulate(df, headers='keys')
        with open(filename, 'w') as f:
            f.write(s)

        print('Equation system saved to file {}.'.format(filename))

        return


def main(args):
    with open(args.prob_matrix) as pm, open(args.coeffs_k) as ck,\
            open(args.coeffs_l) as cl, open(args.filemap) as fmap:
        pm = ProbabilityMatrix(pm, ck, cl, fmap)

    # filename = '05-res-eq-sys.txt'
    time = datetime.datetime.utcnow()
    time_str = time.strftime('%Y-%m-%dT%H%M%S')
    filename = '05-res-eq-sys-' + time_str + '.txt'
    pm.dump_eq_sys_coeffs(filename)

    print('n_vals_op = {},\nn_vals_io = {}'.format(pm.n_vals_op, pm.n_vals_io))
    print('theta_primary = {}'.format(pm.calc_theta_primary()))
    print('N_h = {}'.format(pm.calc_avg_calls_all_files()))
    print('theta_h = {}'.format(pm.calc_avg_infocount_all_files()))
    print('theta_0 = {}'.format(pm.calc_theta_0()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('prob_matrix')
    parser.add_argument('coeffs_k')
    parser.add_argument('coeffs_l')
    parser.add_argument('filemap')
    parser.add_argument('-p', '-print', action='store_true')

    args = parser.parse_args()

    main(args)
