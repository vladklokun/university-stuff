import itertools as it
import neuron as n


DATASET = [1.19, 5.61, 0.89, 6.00, 1.04, 5.98, 0.03, 6.00, 1.83, 4.23, 0.60, 4.15, 0.13, 5.01, 1.87]


def group_n_wise(iterable, n=2):
    t = it.tee(iterable, n)

    for idx, _ in enumerate(t, start=1):
        for subset in t[idx:]:
            next(subset, None)

    return zip(*t)


def main():

    nn = n.NeuralNetwork.random(inputs=3,)

    # Split the dataset into train and test iterators
    # These iterators are 3-wise subsets of the original dataset
    train = group_n_wise(DATASET[:13], 3)
    test = group_n_wise(DATASET[:13], 3)
    # Split the target values too, since they come from the original dataset
    train_target, test_target = DATASET[1:13], DATASET[13:]

    for i, target in zip(train, train_target):
        out = nn.train(i, target)
        print(
            "Training on input: {} (target {}): {}"
            .format(i, target, out)
        )

    for i, target in zip(test, test_target):
        prediction = nn.predict(i)
        print(
            "Predict({}) = {}"
            .format(i, prediction)
        )


if __name__ == "__main__":
    main()
