#Método da aceitação-rejeição
import numpy as np
import matplotlib.pyplot as plt

n = 100000 #numero de amostras
xfunction = np.array([])

for i in range(n):
    x1 = np.random.uniform(0, 1)
    x2 = np.random.uniform(0, 1)

    while (x2 >= (6.75) * x1 * pow((1 - x1), 2)): # f(x)/cg(x)
        x1 = np.random.uniform(0, 1)
        x2 = np.random.uniform(0, 1)
    xfunction = np.append(xfunction, x1)#PDF gerada pelo método da aceitação-rejeição

print(xfunction)
X = np.arange(0, 1, 0.01)
fx = 12 * X * pow((1 - X), 2)#f(x) PDF analítica
#fx1=fx/np.max(fx)
plt.title('PDF analitica e histograma')
plt.plot(X, fx)
plt.hist(xfunction, bins=100, density=True) #Plot dos histogramas da PDF gerada
plt.show()