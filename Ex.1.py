#Geração de sinais pseudoaleatórios

import numpy as np
import matplotlib.pyplot as plt

x0=4 #Primeira semente
x00=7 #Segunda semente
x1=np.array([x0])
x11=np.array([x00])
n=16 #amostras
a=5 #Coeficiente multiplicador
m=7 #coeficiente para operação mod
for i in range(n):
    x0=(a*x0)%m#Gerador para primeira semente
    x1=np.append(x1,x0)
    x00 = (a * x00) % m#Gerador para segunda semente
    x11 = np.append(x11, x00)
print(x1)
print(x11)
ind=np.arange(n+1)

fig, (ax1, ax2) = plt.subplots(1,2)

ax1.set_title('X0=2')
ax1.bar(ind, x1)
ax1.set(xlabel='Amostras', ylabel='X(i)')

ax2.set_title('X0=5')
ax2.bar(ind, x11)
ax2.set(xlabel='Amostras', ylabel='X(i)')
plt.show()
