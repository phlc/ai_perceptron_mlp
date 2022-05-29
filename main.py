from tkinter import E
import data_generator as data
import perceptron as p
import mlp
import math


SIZE = 3
OPERATOR = 'XOR'

def main(size, operator):
    (X, y) = data.generator(operator, size)

    limiar = lambda x: 1 if x>=0 else 0
    sigmoid = lambda x: 1 - 1 /(1 + math.exp(x)) if x < 0 else 1 / (1 + math.exp(-x))
    sigmoid_derivative = lambda x: x*(1-x)

    model_perceptron = p.Perceptron(size, limiar, 0.3)

    print(f"\n---- PERCEPTRON TRAINING for {operator.upper()} ----")

    model_perceptron.fit(X, y)

    print(f"\n---- PERCEPTRON TEST for {operator.upper()} ----")
    for input in X:
        print(f"Input: {input}. Output: {model_perceptron.predict(input)}")


    model_mlp = mlp.MLP()
    model_mlp.compile(size, size, sigmoid, sigmoid_derivative)

    print(f"\n---- MLP TRAINING for {operator.upper()} ----")

    model_mlp.fit(X, y)

    print(f"\n---- MLP TEST for {operator.upper()} ----")
    for input in X:
        print(f"Input: {input}. Output: {round(model_mlp.predict(input))}")


main(SIZE, OPERATOR)
