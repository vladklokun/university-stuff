#!/usr/bin/env python3

import argparse

# Returns a list of recognized identifiers from file
def get_identifiers_list(filecontents):
    return filecontents.split()

# Creates an identifier hash table (dictionary) from a list of identifiers
def create_id_table(identifier_list):
    id_table = dict()
    for identifier in identifier_list:
        id_table.update({identifier: hash(identifier)})

    return id_table

# Pretty prints the formed identifier table
def pretty_print_id_table(id_table):
    # Print header
    print('{:<16} {:>19}\n'.format('Identifier', 'Hash'))

    # Print values themselves
    for key, value in id_table.items():
        print('{:<16} {:= #019x}'.format(key, value))

def main(args):
    with open(args.input) as infile:
        filecontents = infile.read()

    identifier_list = get_identifiers_list(filecontents)

    id_table = create_id_table(identifier_list)

    pretty_print_id_table(id_table)

# Parse command-line arguments
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Parse input files (required)
    parser.add_argument('--input', '-i', required=True)
    
    args = parser.parse_args()

    main(args)
