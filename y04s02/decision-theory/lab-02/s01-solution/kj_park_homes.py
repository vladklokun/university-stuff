import argparse
import json
import pyahp


def main(args):
    with open(args.filename) as json_model:
        model = json.load(json_model)

    ahp_model = pyahp.parse(model)
    priorities = ahp_model.get_priorities()
    print(
        "Priorities: {}"
        .format(priorities)
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')

    args = parser.parse_args()
    main(args)
