# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:13:00 2020

@author: Alvaro Guilherme
"""
import numpy as np
from matplotlib import pyplot as plt
import math

#%% A) Distribuição Uniforme
raiz = (math.sqrt(3))
du = np.random.uniform(low=-raiz, high=raiz, size=(10**7,))

#%% B) Distribuição Gaussiana
dg = np.random.normal(0,1,10**7)

#%% C) Distribuição Rayleigh
b = math.sqrt(2/(4-math.pi))
dr = np.random.rayleigh(b, 10**7)

#%% D) Soma de duas variáveis aleatórias com distribuição Gaussiana
dg2 = np.random.normal(0,1,10**7)
dg3 = np.random.normal(2,math.sqrt(5),10**7)
soma = dg2 + dg3

#%% E) Soma de uma variável aleatória com distribuição Gaussianas
dg4 = np.random.normal(0,1,10**7)
du2 = np.random.uniform(low=-2, high=5, size=(10**7,))
soma2 = dg4 + du2

#%% Médias e variâncias
#Médias
m1 = np.mean(du)
m2 = np.mean(dg)
m3 = np.mean(dr)
m4 = np.mean(soma)
m5 = np.mean(soma2)
vetor_medias = [m1,m2,m3,m4,m5]

#Variâncias
v1 = np.var(du)
v2 = np.var(dg)
v3 = np.var(dr)
v4 = np.var(soma)
v5 = np.var(soma2)
vetor_variancias = [v1,v2,v3,v4,v5]

#%% Gráficos PDF 
epdf_du = plt.hist(du, bins=70, rwidth=0.70, density=True)
#plt.show()
aux = (raiz/(10**3))*2
aux2 = -raiz
vetor_aux = []
vetor_aux2 = []
for i in range(0,10**3):
    aux2 += aux
    vetor_aux.append(aux2)
    vetor_aux2.append((1/(raiz-(-raiz))))
x1 = vetor_aux
y1 = vetor_aux2
tpdf_du = plt.plot(x1,y1)
plt.show()
#%%
def gauss(mu,var,x):
    y_gauss = (1/(math.sqrt(2*math.pi*var)))*math.exp(-((x-mu)**2)/(2*var))
    return y_gauss
epdf_dg = plt.hist(dg,bins=70,range=(-4,4),rwidth=0.70, density=True)
#plt.show()
aux = (4/(10**3))*2
aux2 = -4
vetor_aux = []
vetor_aux2 = []
for i in range(0,10**3):
    aux2 += aux
    vetor_aux.append(aux2)
    aux3 = gauss(0,1,vetor_aux[i])
    vetor_aux2.append(aux3)
x2 = vetor_aux
y2 = np.array(vetor_aux2)
tpdf_dg = plt.plot(x2,y2)
plt.show()
# pdf = stats.norm.pdf(,0,1)
# plt.hist(pdf, bins=70, color='red',histtype='step')
#%%
epdf_dr = plt.hist(dr, bins=70, range=(0,7), rwidth=0.70, density=True)
#plt.show()
aux = 7/(10**3)
aux2 = 0
vetor_aux = []
vetor_aux2 = []
b = (math.sqrt(2/(4-math.pi)))
for i in range(0,10**3):
    aux2 += aux
    vetor_aux.append(aux2)
    aux3 = ((vetor_aux[i]/(b)**2)*math.exp((-(vetor_aux[i])**2)/(2*((b)**2))))
    vetor_aux2.append(aux3)
x3 = vetor_aux
y3 = vetor_aux2
tpdf_dr = plt.plot(x3,y3)
plt.show()
# vetor_eixo = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
# plt.xticks(vetor_eixo)
#%%
epdf_soma = plt.hist(soma, bins=70, rwidth=0.70, density=True)
#plt.show()
step = 0.017
vetor_aux = np.arange(-6,11,step)
vetor_aux2 = []
for i in range(0,10**3):
    # aux2 += aux
    # vetor_aux.append(aux2)
    aux3 = gauss(2,5,vetor_aux[i])
    vetor_aux2.append(aux3)
    
x4 = np.array(vetor_aux)
y4 = np.array(vetor_aux2)

def conv(a,b):
    n1 = len(a);
    n2 = len(b);
    k = 0; s = 0;
    z = np.zeros(((n1+n2)-1));
    # while n < ((n1+n2)-1):
    for i in range((n1+n2)-1):
        k = 0        
        while (k < n1):
            if ((i-k) > -1) and ((i-k) < n2):
                s += (a[k]*b[i-k]);
            k += 1;
        z[i] = s;
        s = 0;
        # n += 1;
    return z

step2 = 26/1999
xzao = np.arange(-10.6,15.4,step2)
# y4s = np.convolve(y2,y4,mode='full')
y4s = conv(y2,y4)
y4s *= step2*0.83
step2 *= 0.96
tpdf_soma = plt.plot(xzao,y4s)
plt.show()
#%%
epdf_soma2 = plt.hist(soma2, bins=70, rwidth=0.70, density=True)
#plt.show()
aux = (8/(10**3))*1.625
aux2 = -5
vetor_aux = []
vetor_aux2 = []
for i in range(0,10**3):
    aux2 += aux
    vetor_aux.append(aux2)
    vetor_aux2.append((1/(5-(-2))))
    
x5 = np.array(vetor_aux)
y5 = np.array(vetor_aux2)

step3 = 15/1999
xzao2 = np.arange(-6,9,step3)
# y5s = np.convolve(y2,y5)
y5s = conv(y2,y5)
y5s *= step3
tpdf_soma2 = plt.plot(xzao2,y5s)
plt.show()
#%% Gráficos CDF
ecdf_du = plt.hist(du, bins=70, density=True, histtype='step', cumulative=True)
#plt.show()
z = np.array(y1)
y1c = z.cumsum()
y1c /= y1c[-1]
tcdf_du = plt.plot(x1,y1c)
plt.show()
#%%
ecdf_dg = plt.hist(dg, bins=70, density=True, histtype='step', cumulative=True)
z = np.array(y2)
y2c = z.cumsum()
y2c /= y2c[-1]
tcdf_dg = plt.plot(x2,y2c)
plt.show()
#%%
ecdf_dr = plt.hist(dr, bins=70, density=True, histtype='step', cumulative=True)
z = np.array(y3)
y3c = z.cumsum()
y3c /= y3c[-1]
tcdf_dr = plt.plot(x3,y3c)
plt.show()
#%%
ecdf_soma = plt.hist(soma, bins=70, density=True, histtype='step', cumulative=True)
y4c = y4s.cumsum()
y4c *= step2
# y4c /= y4c[-1]
tcdf_soma = plt.plot(xzao,y4c)
plt.show()
#%%
ecdf_soma2 = plt.hist(soma2, bins=70, density=True, histtype='step', cumulative=True)
y5c = y5s.cumsum()
y5c *= step3
# y5c /= y5c[-1]
tcdf_soma = plt.plot(xzao2,y5c)
plt.show()
#%% Teste
#np.arange()
#fig,ax = subplot()
#ax.plot()
#ax.set_yscale()
# a = "a"
# x = "1"
# y = int(x)
# b = a+x
# print (b)
# print (y+1)
# vetor = []
# for i in range(0,10):
#     vetor.append(i) 
#     print (i)
# print (vetor)    
# print(math.exp(1))
# epdf_dg2 = plt.hist(dg3, bins=70, rwidth=0.70, histtype='bar', density=True)
# print (np.array(zz).cumsum())
# zzz = [1,2,3,4,5,6,7]
# zzz = np.array(zzz)
# zzz = zzz/zzz[-1]
# print (zzz)
# print (zzz[-2])
# metodo, tempo = signal.choose_conv_method(y2,y5,measure=True)
# a = [1,2,3,4,5]
# b = [2,4,6,8,10]
# b1 = [10,8,6,4,2]
# c = [2,1,0,-1,-2]
# a = np.array(a)
# b = np.array(b)
# c = np.array(c)
# print (np.flip(4-b))
# c += 1
# # plt.plot(b,a)
# # plt.show()
# # plt.plot(c,a)
# # plt.show()
# # print (signal.convolve(a,b,mode='valid'))
# n = 0
# d = []
# def flipar(n,b):
#     for i in range(len(b)):
#         if i < ((len(b))/2):
#             h = b[i]
#             b[i] = b[n-(i+1)]
#             b[n-(i+1)] = h
#     return b

# def conv(a,b):
#     d = (np.dot(a,b))
#     return d

# for i in range(len(b)):
#     print(n)
#     b = flipar(n,b)
#     d.append(conv(a,b))
#     n += 1

# print(d)
# print(np.dot(a,b1))

# for i in range(len(b)):
#     b = flipar(n,b)
#     n += 1
# flip = flipar(n,b)
# print (flip)
# print(len(b)%2)
# def integrand(x):
#     return x**2
# result = integrate.quad(integrand,-(np.inf),2)