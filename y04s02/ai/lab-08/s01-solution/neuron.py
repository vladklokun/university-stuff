import typing as typ
import logging

logger = logging.basicConfig(level=logging.WARNING)


def act_func_linear(S: int, threshold: float):
    if S < threshold:
        return 0
    else:
        return 1


def act_func_logistic(S: int, threshold: float):
    if S < threshold:
        return 0
    else:
        return 1


class MPNeuron(object):

    def __init__(
        self,
        weights: typ.List[int],
        threshold: int,
        act_func: typ.Callable[[int], bool] = act_func_linear,
        name: str = "",
    ):
        self.weights = weights
        self.act_func = act_func
        self.threshold = threshold
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod
    def _weighted_sum(weights, inputs):
        logging.debug(
            "Weights = {}\n"
            "Inputs = {}"
            .format(weights, inputs)
        )
        weighted_inputs = [x_n * w_n for x_n, w_n in zip(inputs, weights)]
        logging.debug(
            "Weighted = {}".format(weighted_inputs)
        )
        S = sum(weighted_inputs)
        logging.debug("S = {}".format(S))
        return S

    def eval(self, *inputs):
        S = self._weighted_sum(self.weights, inputs)
        res = self.act_func(S, self.threshold)
        return res


class ForwardPropagationNeuralNet(object):

    @classmethod
    def from_list(
        cls,
        layer_list: typ.List[typ.List[typ.Tuple]],
        name: str = ""
    ):
        """Constructs a neural network from its' neurons specifications.
        """
        layers = []
        for layer in layer_list:
            layer_neurons = []
            for weights, threshold in layer:
                n = MPNeuron(weights=weights, threshold=threshold)
                layer_neurons.append(n)

            layers.append(layer_neurons)

        return cls(layers=layers, name=name)

    def __str__(self):
        return self.name

    def __init__(self, layers: typ.List[typ.List[MPNeuron]], name: str = ""):
        self.layers = layers
        self.name = name

    def eval(self, *inputs):
        """Evaluates the result of the neural network on given inputs."""
        next_inputs = [*inputs]
        for layer in self.layers:
            next_inputs = [neuron.eval(*next_inputs) for neuron in layer]

        return next_inputs
