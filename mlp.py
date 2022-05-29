import math
import numpy as np
from matplotlib import pyplot as plt

class Neuron:
    def __init__(self, function, number_inputs):
        self.function = function
        self.output = 0.0
        self.error = 0.0
        self.weights = np.random.uniform(-1, 1, number_inputs)
        self.bias = np.random.uniform(-1, 1, size=None)


    def forward(self, inputs):
        self.output = self.bias
        self.output += np.sum(np.multiply(inputs, self.weights))
        self.output = self.function(self.output)
        return self.output


class MLP:
    def __init__(self):
        self.hidden_layer = []
        self.output_layer = None
        self.function_derivative = None
        self.learning_rate = None
    

    def compile(self, number_inputs, number_neurons_hidden, function, function_derivative, rate=0.3):
        self.function_derivative = function_derivative
        self.learning_rate = rate
        for i in range(number_neurons_hidden):
            self.hidden_layer.append(Neuron(function, number_inputs))
        
        self.output_layer = Neuron(function, number_neurons_hidden)

    def fit(self, X, y, epochs=10000):
        print("Training Model")
        erros = 0;
        for i in range(epochs):
            erros = 0
            for j in range(len(X)):
                resposta = self.predict(X[j])
                desejada = y[j]
                if(round(resposta) != desejada): 
                    erros += 1

                #Erro - Camada Saída
                self.output_layer.error = (resposta - desejada)*self.function_derivative(resposta)

                #Erro - Camada Oculta
                for k in range(len(self.hidden_layer)):
                    self.hidden_layer[k].error = (self.output_layer.weights[k]*self.output_layer.error)*self.function_derivative(self.hidden_layer[k].output)
                #Recalculo Pesos - Camada Saída
                for k in range(len(self.output_layer.weights)):
                    self.output_layer.weights[k] = self.output_layer.weights[k] - self.learning_rate*self.hidden_layer[k].output*self.output_layer.error
                self.output_layer.bias = self.output_layer.bias - self.learning_rate*self.output_layer.error

                #Recalculo Pesos - Camada Saída
                for k in range(len(self.hidden_layer)):
                    for m in range(len(self.hidden_layer[k].weights)):
                        self.hidden_layer[k].weights[m] = self.hidden_layer[k].weights[m] - self.learning_rate*X[j][m]*self.hidden_layer[k].error
                    self.hidden_layer[k].bias = self.hidden_layer[k].bias - self.learning_rate*self.hidden_layer[k].error
                    
            
            if (erros==0):
                print("Model Trained - Erros: 0")
                break
        if(erros != 0):
            print(f"Model Trained - Failed to reach 0 erros - Erros: {erros}")
        

    def predict(self, X):
        next_layer_input = []
        for i in range(len(self.hidden_layer)):
            next_layer_input.append(self.hidden_layer[i].forward(X))

        return self.output_layer.forward(next_layer_input)
            
        


