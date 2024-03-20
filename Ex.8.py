import numpy as np
import matplotlib.pyplot as plt

n = 100000 # número de amostras
xfunction = np.array([])

for i in range(n):
    x1 = np.random.uniform(-1, 1)
    x2 = np.random.uniform(0, 2) # cg(x) = 2

    while (x2 >= 1.5 * x1**2): # f(x)/cg(x)
        x1 = np.random.uniform(-1, 1)
        x2 = np.random.uniform(0, 2)

    xfunction = np.append(xfunction, x1)

# Plotar a PDF analítica e o histograma das amostras geradas
X = np.linspace(-1, 1, 1000)
fx = 1.5 * X**2 # PDF analítica

plt.title('PDF analítica e histograma')
plt.plot(X, fx, label='PDF analítica')
plt.hist(xfunction, bins=100, density=True, label='Histograma normalizado') # Plot do histograma das amostras
plt.legend()
plt.show()
