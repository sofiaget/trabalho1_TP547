# V.A. binomial
import numpy as np
import matplotlib.pyplot as plt

q=0.12#Probabilidade de um pistao ser rejeitado
n=8 #Número de pistoes
value1=3 #não mais que 3 rejeitados
value2=7 #pelo menos 7 rejeitados
N=100000#Número de amostras
c = q/(1-q)
av=np.array([])
count=0
x=np.random.uniform(0,1,N)
for ix in x:
    i = 0
    pr = pow((1 - q),n)
    F = pr
    while ix>=F:
        pr = (c * (n - i) / (i + 1))* pr;
        F = F + pr;
        i = i + 1;
    a1=i
    av=np.append(av,a1)

print(av)

for binvalue in av:
    if binvalue<=value1: #Para x<=3. Para a probabilidade de não mais que 3 rejeitados
        count=count+1
prob=count/N
print("a probabilidade de nao mais que tres rejeitados e",prob)

count=0
for binvalue in av:
    if binvalue>=value2:#Para x>=7. Para a probabilidade de ao menos 7 rejeitados
        count=count+1
prob1=count/N
print("a probabilidade de pelo menos sete rejeitados e",prob1)

#plot histograma variavel


plt.title('Distruicao binomial para n=8')
plt.hist(av,bins=100,density=True)
plt.xlabel('Pistoes rejeitados')
plt.ylabel('X(i)')
plt.show()
