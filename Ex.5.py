#V.A. exponencial

import numpy as np
import matplotlib.pyplot as plt


N=100000 #numero de amostras
lambda1=1/28 #numero de passagens a cada 28 dias
x=np.random.uniform(0,1,N)
value=4 #comprar uma passagem com menos de 4 dias de antecedencia
Xexp=-np.log(1-x)/lambda1 #Geração de variável distribuida expoencialmente pelo método da inversa
count=0
print(Xexp)


for expvalue in Xexp:
    if expvalue<value: # menos que 4 dias de antecedencia
        count=count+1
prob=count/N
print("a probabilidade e",prob)

Probana=1-np.exp(-lambda1*value)  #CDF da distribuição exponencial. Cálculo da probabilidade analítica
print("a probabilidade analítica e",Probana)

#plot pdf

X=np.arange(0, 120, 0.1) #Vetor para plot da variável exponencial
fx=lambda1*np.exp(-lambda1*X) #pdf da V.A. exponencial
plt.plot(X,fx)
plt.show()

