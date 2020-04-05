import logging
logging.basicConfig(level=logging.WARNING)

import typing as typ
import math
import random


def logistic(s: float) -> float:
    res = 1 / (1 + math.exp(-s)) * 10
    return res


def logistic_prime(s: float) -> float:
    numerator = math.exp(-s)
    denominator = (1 + math.exp(-s))**2
    res = numerator / denominator
    return res


class Neuron(object):

    @classmethod
    def random(cls, inputs: int = 3):
        weights = [
            random.random()
            for _ in range(inputs)
        ]
        return cls(weights=weights)

    def __init__(
        self,
        weights: typ.List[float],
        act_fn: typ.Callable[[float], float] = logistic,
        act_fn_prime: typ.Callable[[float], float] = logistic_prime,
        name: str = "",
    ):
        self.weights = weights
        self.act_fn = act_fn
        self.act_fn_prime = act_fn_prime
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod
    def _calc_weighted_sum(weights: typ.List[float], inputs):
        logging.debug(
            "Weights = {}\n"
            "Inputs = {}"
            .format(weights, inputs)
        )
        weighted_inputs = [w_n * x_n for w_n, x_n in zip(weights, inputs)]
        logging.debug(
            "Weighted = {}".format(weighted_inputs)
        )
        weighted_sum = sum(weighted_inputs)
        logging.debug("weighted_sum = {}".format(weighted_sum))
        return weighted_sum

    def calc_output(self, inputs):
        weighted_sum = self._calc_weighted_sum(self.weights, inputs)
        output = self.act_fn(weighted_sum)
        return output

    def calc_error_pd(
        self,
        input_val: float,
        output_val: float,
        target: float,
        weighted_sum: float,
    ):
        diff = output_val - target
        derivative = self.act_fn_prime(weighted_sum)
        error_pd = diff * derivative * input_val
        return error_pd

    def calc_error_pds(self, inputs, outputs, target):
        weighted_sum = self._calc_weighted_sum(
            weights=self.weights,
            inputs=inputs
        )

        error_pds = []
        for input_val, output_val in zip(inputs, outputs):
            delta = self.calc_error_pd(
                input_val=input_val,
                output_val=output_val,
                target=target,
                weighted_sum=weighted_sum,
            )
            error_pds.append(delta)

        logging.debug("Error_pds = {}".format(error_pds))
        return error_pds

    def update_weights(self, weight_delta):
        for idx, w in enumerate(self.weights):
            self.weights[idx] += weight_delta


class NeuralNetwork(object):

    @classmethod
    def random(cls, inputs=3):
        neurons = [Neuron.random()]
        obj = cls(neurons=neurons)
        return obj

    def __init__(
        self,
        neurons: typ.List[Neuron],
        learning_speed: float = 0.35,
    ):
        self.neurons = neurons
        self.learning_speed = learning_speed

    def feed_forward(self, inputs):
        outputs = []
        for neuron in self.neurons:
            out = neuron.calc_output(inputs)
            outputs.append(out)

        return outputs

    def feed_backward(self, inputs, output, target):
        for n in self.neurons:
            error_pds = n.calc_error_pds(
                inputs=inputs,
                outputs=output,
                target=target
            )
            weight_deltas = [-self.learning_speed * e for e in error_pds]
            weight_delta_avg = sum(weight_deltas) / len(weight_deltas)
            n.update_weights(weight_delta_avg)

    def train(self, training_input, target):
        output = self.feed_forward(training_input)
        logging.debug(
            "Input: {} Target: {} Output: {}"
            .format(training_input, target, output)
        )
        self.feed_backward(training_input, output, target)
        return output

    def predict(self, inputs):
        return self.feed_forward(inputs)
