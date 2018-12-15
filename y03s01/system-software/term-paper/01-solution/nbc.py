# This is a Naive Bayes Classifier implementation in Python
# written by Vlad Klokun and Igor Rabin
#
# Inputs: a CSV data file that contains training data
# Does: analyzes given CSV training file according to the Naive Bayes Classifier algorithm, generates random data and then makes a prediction about it
#
# Assumes a Gaussian Distribution

#!/usr/bin/env/ python3

import csv # reading CSV files
import random # list shuffling
import math # exp, pow etc

# Loads a valid CSV file containing floating-point training data into memory
# Input: a filename of a training file in CSV format
# Output: a dataset in form of a list of floats
def load_training(filename):
    with open(filename) as file:
        # ignore all lines which start with '#'
        reader = csv.reader(row for row in file if not row.startswith('#'))
        dataset = []
        for row in reader:
            # comprehend each line as a list of floats and append it to the dataset
            dataset.append([float(x) for x in row])

    return dataset

# split_dataset() splits a given dataset into 'training' and 'test' datasets to test the algorithm
# Inputs: a dataset (list), split_ratio (float)
# Outputs: a tuple of: dataset_train --- training dataset (list), dataset_test --- dataset (list)
def split_dataset(dataset, ratio):
    dataset_shuffled = dataset
    random.shuffle(dataset_shuffled)
    dataset_train = dataset_shuffled[len(dataset_shuffled) // ratio:]
    dataset_test = dataset_shuffled[:len(dataset_shuffled) // ratio]

    return dataset_train, dataset_test

# Separate entries by class. Assumes that class is the last parameter
# Input: dataset
# Output: dictionary with class as key and matching entries as values
def separate_by_class(dataset):
    separated = {}
    for entry in dataset:
        # if entry with a given label is not yet in the dictionary, add it
        if entry[-1] not in separated:
            separated[entry[-1]] = []

        separated[entry[-1]].append(entry)

    return separated

# calc_mean(): Calculates mean value of a given sequence
# Inputs: seq — a sequence of numbers
# Outputs: a mean value of the sequence (float)
def calc_mean(seq):
    return sum(seq) / len(seq)

# calc_variance(): Calculates variance of a given sequence
# Input: seq --- a sequence of numbers
# Output: variance --- variance value (sigma^2) computed using n - 1 estimator
def calc_variance(seq):
    if len(seq) == 1:
        return 0
    # expected value
    mean = calc_mean(seq)
    # the variance of the set assuming all values are equally likely
    # use n - 1 estimator
    variance = sum([pow(x - mean, 2) for x in seq]) / (len(seq) - 1)
    # return math.sqrt(variance)
    return variance

# summarize(): summarizes every attribute in a dataset with their probabilistic properties: mean and variance. Makes no distiction based on class variables. returns a list of tuples which contain mean and variance values for respective attributes
# Input: dataset --- a list containing a dataset
# Output: summaries --- a list of tuples with statistical properties for each attribute in form of (mean, variance)
def summarize(dataset):
    summaries = []
    for attribute in zip(*dataset):
        summaries.append((calc_mean(attribute), calc_variance(attribute)))

    # removes summary for last column — class
    del summaries[-1]
    return summaries

# summarize_by_class(): summarizes every attribute in a dataset with their probabilistic properties: mean and variance. Unlike summarize(), the attributes are summarized on a per-class basis. Returns a list of tuples which contain mean and variance values for respective attributes belonging to certain classes.
# Input: dataset --- a dataset
# Output: summaries --- a dictionary with class variables as keys and statistical summaries of attributes as values
def summarize_by_class(dataset):
    separated = separate_by_class(dataset)
    summaries = {}
    for class_value, data in separated.items():
        summaries[class_value] = summarize(data)

    return summaries

# calculate_probability(): calculates probability of a given value X belonging to a certain class, assuming Gaussian distribution and passed mean and variance values
# Input 1: x --- value to be tested for belonging to a certain class
# Input 2: mean --- mean value for an attribute which the value is tested against
# Input 2: variance --- variance value for an attribute which the value is tested against
def calculate_probability(x, mean, variance):
    # if variance = 0 attribute values are the same and testing doesn't really make sense
    if variance == 0:
        return 0
    exp = math.exp( (-math.pow(x - mean, 2) ) / (2 * variance) )
    return (1 / math.sqrt(2 * math.pi * variance)) * exp

# calc_class_probability(): calculates probabilities of given input vector belonging to every class
# Input 1: summaries --- list of statistical summaries for every class
# Input 2: input_vector --- an entry to be classified
# Output: probabilities --- a dictionary containing probabilities of an entry belonging to each class
def calc_class_probability(summaries, input_vector):
    probabilities = {}
    for class_value, summaries in summaries.items():
        probabilities[class_value] = 1
        for (mean, variance), x in zip(summaries, input_vector):
            probabilities[class_value] *= calculate_probability(x, mean, variance)

    return probabilities

# predict(): predicts the class of a given entry
# Input 1: summaries --- list of statistical summaries for every class
# Input 2: input_vector --- an entry to be classified
# Output 1: key value of a class to which given entry most possibly belongs
def predict(summaries, input_vector):
    probabilities = calc_class_probability(summaries, input_vector)
    # get key with max value
    return max(probabilities, key = probabilities.get)

# predict_dataset(): makes predictions for a whole given dataset
# Input 1: summaries --- list of statistical summaries for every class
# Input 2: dataset --- a dataset to be classified
# Output 1: predictions --- a list of class values, to which entries are predicted to belong
def predict_dataset(summaries, dataset):
    predictions = []
    for entry in dataset:
        predictions.append(predict(summaries, entry))

    return predictions

# compute_accuracy(): computes accuracy of predictions given the dataset with known-good class variables
# Input 1: dataset --- a dataset with known-good classification
# Input 2: predictions --- a list of predictions made by the Native Bayes Classifier
# Output 1: accuracy in %
def compute_accuracy(dataset, predictions):
    correct = 0
    for entry, prediction in zip(dataset, predictions):
        # c_act --- actual known-good class, c_pred --- class predicted by Naive Bayes Classifier
        print('Entry: "{}", c_act: "{}", c_pred: "{}"'.format(entry, entry[-1], prediction))
        # print('Entry: "{}",\nActual Class: "{}",\nPredicted Class: "{}"'.format(entry, entry[-1], prediction))
        if entry[-1] == prediction:
            correct += 1

    return (correct / len(dataset)) * 100.0

