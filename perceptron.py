import numpy as np

class Perceptron:

    def __init__ (self, entradas, funcao, taxa):
        self.pesos = np.random.uniform(-1, 1, entradas+1)
        self.funcao = funcao
        self.taxa = taxa


    def predict(self, X):
        X_bias = [self.bias] + X
        somatorio = np.sum(np.multiply(X_bias, self.pesos))
        return self.funcao(somatorio)


    def fit(self, X, y, epochs=9, bias=1):
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
            print(f"Epoch {i+1} - Erro: {erros/len(X)}")




X = [[0, 0],
     [0, 1],
     [1, 0],
     [1, 1]]

y_and = [0, 0, 0, 1]
y_or  = [0, 1, 1, 1]
y_xor = [0, 1, 1, 0]

print("---- AND ----")
model_and = Perceptron(2, lambda x: 1 if x>=0 else 0, 0.3)
model_and.fit(X, y_and)
for instance in X:
    print(f"Entrada: {instance}. Saída: {model_and.predict(instance)}")

print("\n---- OR ----")
model_or = Perceptron(2, lambda x: 1 if x>=0 else 0, 0.3)
model_or.fit(X, y_or)
for instance in X:
    print(f"Entrada: {instance}. Saída: {model_or.predict(instance)}")

print("\n---- XOR ----")
model_xor = Perceptron(2, lambda x: 1 if x>=0 else 0, 0.3)
model_xor.fit(X, y_xor)
for instance in X:
    print(f"Entrada: {instance}. Saída: {model_xor.predict(instance)}")