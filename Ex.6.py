# V.A. geométrica

import numpy as np
import matplotlib.pyplot as plt

p=0.4#Probabilidade de sair bola preta
value=6 #tirar a bola preta na sexta tentativa
N=100000#Número de amostras
count=0

av=np.array([])
x=np.random.uniform(0,1,N) #geração da V.A. uniforme entre 0 e 1, com N amostras

for ix in x:

    i = 1                      #Inicialização da variável i=1
    pr = p                     #Cálculo da probabilidade para x=1, parcela (1-p)**x-1 vai para zero
    F=pr                       #Atribuição do resultado na variável F
    while ix>=F:               #Enquanto o valor do laço for maior do que F
        pr=(1-p)*pr            #Calcula probabilidade a cada iteração
        F = F + pr             #Soma o valor de F à probabilidade encontrada pela forma recursiva
        i = i + 1;             #Incrementa a variável i
    a1=i
    av=np.append(av,a1)        #Adiciona os valores de i na matriz av

print(av)

for geovalue in av:            #Cálculo da probabilidade para cada valor gerado geométrica
    if geovalue==value:        #Se o valor gerado da distribuição geométrica é 6, incrementa a variável count
        count=count+1
prob=count/N                   #Probabilidade entre 0 e 1 será o valor de count dividido pelo número de amostras
print("a probabilidade é",prob)

Probana=p*((1-p)**(value-1))       #Calcula probabilidade de forma analítica
print("a probabilidade analítica e",Probana)
