import itertools as it
import neuron as n

XOR_LAYER_LIST = [
    [
        ([1, -1], 0.5), # Neuron 1,
        ([-1, 1], 0.5)  # Neuron 2
    ],
    [
        ([1, 1], 0.5)
    ]
]

FX_NEURON = {
    "weights": [-1, 1, 1],
    "threshold": 0,
}

def test_neuron(n, input_count: int = 2):
    for inputs in it.product([0, 1], repeat=input_count):
        res = n.eval(*inputs)
        print(
            "Evaluating {}({}) = {}"
            .format(n, inputs, res)
        )

def main(*args, **kwargs):
    # Task 1: model an AND logic gate
    and_func = n.MPNeuron(
        weights=[1, 1],
        threshold=1.5,
        name="AND",
    )
    test_neuron(and_func)

    # Task 2: model an OR logic gate
    or_func = n.MPNeuron(
        weights=[1, 1],
        threshold=0.5,
        name="OR",
    )
    test_neuron(or_func)


    # Task 3: model a NOT logic gate
    not_func = n.MPNeuron(
        weights=[-1.5],
        threshold=-1,
        name="NOT",
    )
    test_neuron(not_func, input_count=1)

    # Task 4: model a XOR logic gate
    layer_list = [
        [
            ([1, -1], 0.5), # Neuron 1,
            ([-1, 1], 0.5)  # Neuron 2
        ],
        [
            ([1, 1], 0.5)
        ]
    ]
    xor_nn = n.ForwardPropagationNeuralNet.from_list(
        layer_list=layer_list, name="XOR"
    )
    test_neuron(xor_nn)

    # Task 5: Model F(x_1, x_2, x_3)
    fx_neuron = n.MPNeuron(**FX_NEURON, name="F")
    test_neuron(fx_neuron, input_count=3)

if __name__ == "__main__":
    main()
