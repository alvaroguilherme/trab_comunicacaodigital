# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 12:17:19 2020

@author: Alvaro Guilherme
"""

import numpy as np
from matplotlib import pyplot as plt

#%% Sequência A
r = np.random.randn(10**7)
def norm(s):
    z = []
    for i in range(len(s)):
        if s[i] > 0:
            z.append(1)
        else:
            z.append(-1)
    z = np.array(z)
    return z

x = norm(r)

#%% A) A/dp = 1
# Sequência Gaussiana
def seq(dp):
    # Sequência Gaussiana
    v = np.random.normal(0,dp,10**7)
    
    # Soma
    y = x + v
    
    # PDFs
    plt.hist(x, bins=50, density=True)
    plt.show()
    plt.hist(v, bins=50, rwidth=0.50, density=True)
    plt.show()
    plt.hist(y, bins=50, rwidth=0.50, density=True)
    plt.show()
            
    return y    
 
def erro(n):           
    bits_e = 0
    nb = 0
    n = norm(n)
    for i in range(len(n)):
        nb += 1
        if (n[i]!=x[i]):
            bits_e += 1
    return (bits_e/nb)
       
dp = 1
a = seq(dp)
ae = erro(a)

#%% B) A/dp = 1/2
dp = 2
b = seq(dp)
be = erro(b)

#%% C) A/dp = 1/8
dp = 8
c = seq(dp)
ce = erro(c)

#%% D) A/dp = 1/32
dp = 1/32
d = seq(dp)
de = erro(d)

#%% Gráfico BER
ax_x = [1/32,1/8,1/2,1]
ax_y = [de,ce,be,ae]
plt.plot(ax_y,ax_x)
plt.yscale('log')
#%%
print (ae,be,ce,de)
#%% Teste
#print (s[-1])
# e = [1,2,3]
# e = np.array(e)
# f = [1,4,3]
# f = np.array(f)
# print (e^f)