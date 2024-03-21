#Variavel aleatoria de poisson
import numpy as np
import matplotlib.pyplot as plt


lambda1=6 #Número médio de chamadas em uma hora
N=100000 #Numero de amostras
value1=0 #nao receber nenhuma chamada em uma determinada hora
value2=8 #receber menos de oito chamadas em uma determinada hora
count=0
av=np.array([])
x=np.random.uniform(0,1,N) #geração de uma variável aleatória uniforme
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
    if poissonvalue==value1: #Para x=0, nenhuma chamada recebida
        count=count+1
prob=count/N
print("a probabilidade de nenhuma chamda e",prob)

count=0
for poissonvalue1 in av:
    if poissonvalue1<value2: #para x<8, probabilidade de receber  menos que 8 chamadas. 
        count=count+1
prob1=count/N #Probabilidade de receber menos que 8 chamadas
print("a probabilidade de mais de sete chamadas e",prob1)

m=lambda1 #media
v=lambda1 #variancia
dp=v**(0.5) #desvio padrao

print("a media e",m)
print("a variancia e",v)
print("o desvio padrao e",dp)
