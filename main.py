from tkinter import E
import data_generator as data
import perceptron as p
import mlp
import math


SIZE = 5
OPERATOR = 'XOR'

def main(size, operator):
    (X, y) = data.generator(operator, size)

    limiar = lambda x: 1 if x>=0 else 0
    sigmoid = lambda x: 1 - 1 /(1 + math.exp(x)) if x < 0 else 1 / (1 + math.exp(-x))
    sigmoid_derivative = lambda x: sigmoid(x)*(1-sigmoid(x))

    model = p.Perceptron(size, limiar, 0.3)

    model.fit(X, y)

    print(f" ---- {operator.upper()} ----")
    for input in X:
        print(f"Input: {input}. Output: {model.predict(input)}")


main(SIZE, OPERATOR)
