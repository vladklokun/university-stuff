#!/usr/bin/env python3

import argparse
from nbc import *

def main(args):
    dataset = load_training(args.input)
    dataset_train, dataset_test = split_dataset(dataset, 1/3) # split dataset 1 / 3

    summaries = summarize_by_class(dataset_test)
    predictions = predict_dataset(summaries, dataset_test)
    acc = compute_accuracy(dataset_test, predictions)
    print('Accuracy: {}'.format(acc))

    print('len(train) = {}, len(test) = {}'.format(len(dataset_train), len(dataset_test)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'An implementation of Gaussian Naive Bayes Classifier in Python using stdlib facilities. Reads a CSV file containing floats.')

    # Parse CSV dataset file
    parser.add_argument('input', help = 'Path to input file')
    
    args = parser.parse_args()

    main(args)
