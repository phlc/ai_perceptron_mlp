import numpy as np

class Perceptron:

    def __init__ (self, entradas, funcao, taxa=0.3):
        self.pesos = np.random.uniform(-1, 1, entradas+1)
        self.funcao = funcao
        self.taxa = taxa


    def predict(self, X):
        X_bias = [self.bias] + X
        somatorio = np.sum(np.multiply(X_bias, self.pesos))
        return self.funcao(somatorio)


    def fit(self, X, y, epochs=100, bias=1):
        print("Training Model")
        erros = 0
        self.bias = bias
        for i in range(epochs):
            erros = 0
            for j in range(len(X)):
                resposta = self.predict(X[j])
                desejada = y[j]
                if(resposta != desejada): 
                    erros += 1
                X_bias = [bias] + X[j]
                for k in range(len(self.pesos)):
                    self.pesos[k] = self.pesos[k] + self.taxa*(desejada - resposta)*X_bias[k]
            if (erros==0):
                print("Model Trained - Erros: 0")
                break
        if(erros != 0):
            print(f"Model Trained - Failed to reach 0 erros - Erros: {erros}")