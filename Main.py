from Perceptron import Perceptron
from Util import *

def train_perceptron(perceptron, train_set, prnt=False):
    while perceptron.accuracy != 1:
        for i in range(get_dataset_size(train_set)):
            perceptron.train(prnt)


if __name__ == "__main__":
    train, test = file_to_dict("iris_training.txt"), file_to_dict("iris_test.txt")
    learning_rate = 0.01
    perceptron = Perceptron(len(train.keys()), learning_rate)
