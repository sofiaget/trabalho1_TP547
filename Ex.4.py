#V.A. poisson

import numpy as np
import math
import matplotlib.pyplot as plt


lambda1=3 #Número de falhas em uma semana
N=100000 #Numero de amostras
value=2 #ao menos 3 falhas em uma semana
count=0
av=np.array([])
x=np.random.uniform(0,1,N)
for ix in x:
    i = 0
    pr = np.exp(-lambda1)
    F=pr
    while ix>=F:
        pr=lambda1/(i+1)*pr
        F = F + pr
        i = i + 1;
    a1=i
    av=np.append(av,a1)

print(av)

for poissonvalue in av:
    if poissonvalue<value: # probabilidade de ser menor que 2. Prob. de 0 e 1.
        count=count+1
prob=count/N

prob1=1-prob # probilidade de ser maior e igual a 2.
print("a probabilidade e",prob1)

#plot histograma da variavel


plt.title('Distruicao poisson para lambda=3')
#X=np.arange(0, 10, 1)
#fx=np.arange()
'''
for j in X:
    fx[j]=(lambda1**X*np.exp(-lambda1))/(math.factorial(X[j])) #pdf da V.A. de poisson
plt.bar(X, fx)
'''

plt.hist(av,bins=100,density=True)
plt.xlabel('falhas')
plt.ylabel('X(i)')
plt.show()
