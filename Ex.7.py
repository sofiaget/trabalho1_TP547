#Método da transformada inversa

import numpy as np
import matplotlib.pyplot as plt


N=100000 #numero de amostras
x=np.random.uniform(0,1,N) #gerador da distribuição uniforme normalizado

Xexp=np.log((x*(np.exp(1)-1))+1)#expressão com o x isolado

print(Xexp)
X=np.arange(0, 1, 0.01)
fx=np.exp(X)/(np.exp(1)-1)#PDF analítica
#fx1=fx/np.max(fx)
plt.figure()
plt.title('PDF analitica e histograma')
plt.plot(X,fx) #plot da pdf analitica
#plt.figure()
plt.hist(Xexp,bins=100,density=True)#histograma normalizado
plt.show()