from Util import *
class Perceptron:
    def __init__(self, num_attributes, learning_rate):
        self.num_attributes = num_attributes
        # self.X = []
        self.weights = [1 for i in range(num_attributes)]
        self.bias = 0
        self.learning_rate = learning_rate
        self.iterations = 0
        self.accuracy=0

    def train(self, X, prnt):

        self.iterations += 1
        pass
    def classify(self, X):
        pass

    def multiply_vectors(self, v1, v2):
        if len(v1)!= len(v2):
            print(f"Error: vector lengths do not match \n{v1} (length {len(v1)}) and {v2} (length {len(v2)}))")
        result =[]
        for i in range(len(v1)):
            result.append(v1[i]*v2[i])
        return result

    def print_state(self):
        print("Iterations: ", self.iterations, " Weights: ", self.weights, ", Bias: ", self.bias)