# -*- coding: utf-8 -*-
import csv


class SystemStats(object):
    def __init__(self, stats, system_type):
        self.stats = stats
        self.system_type = system_type

    @staticmethod
    def print_stats_header():
        print(
            '{:>6} {:>6} {:>10} {:>12} {:>10} {:>8} {:>10}'
            .format(
                'Step #', 'CPUs', 'Diameter', 'Diameter_Avg', 'Degree', 'Cost',
                'Traffic'
            )
        )

    def print(self):
        """ Pretty-print scaling stats """
        self.print_stats_header()
        for s in self.stats:
            print(
                '{step:>6} {node_count:>6} {diameter:>10} '
                '{avg_diameter:>12.4f} {degree:>10} {cost:>8} {traffic:>10.4f}'
                .format(
                    **s
                )
            )

    def to_csv(self, filename):
        """ Write the stats to a CSV file """

        # Field names are names of the stats
        field_names = self.stats[0].keys()

        # Do not leave empty lines between rows
        with open(filename, 'w', newline='') as csvf:
            writer = csv.DictWriter(csvf, fieldnames=field_names)

            writer.writeheader()
            for s in self.stats:
                writer.writerow(s)
