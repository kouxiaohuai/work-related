# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:35:02 2019

@author: kWX596514
"""

import math
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


d1 = 200
d2 = (1000**2+500**2)**0.5
h = 61.47
f = 800
c = 3 * 10**8
λ = c / 10**6 / f
n = 10**4


def single_knife_edge_model(ν):
#    ν = h * (2/λ*(1/d1+1/d2))**0.5
    '''
    def re(x):
        return math.cos(math.pi*x**2/2)
    C, err = integrate.quad(re, 0, ν)
    def im(x):
        return math.sin(math.pi*x**2/2)
    S, err = integrate.quad(im, 0, ν)
    '''
    C, S = 0, 0
    for i in np.linspace(0, ν, n):
        C = C + math.cos(math.pi*i**2/2)*(ν-0)/n
        S = S + math.sin(math.pi*i**2/2)*(ν-0)/n
    G = -20*math.log10(((1-C-S)**2+(C-S)**2)**0.5/2)
    if ν > -0.78:
        G_approximation = 6.9 + 20*math.log10(((ν-0.1)**2+1)**0.5+ν-0.1)
    else:
        G_approximation = 0
    return G, G_approximation


G = []
G_approximation = []

for i in np.linspace(-5, 45, 1000):
    G.append(single_knife_edge_model(i)[0])
    G_approximation.append(single_knife_edge_model(i)[1])

plt.plot(np.linspace(-5, 45, 1000), [-i for i in G], color='red')
plt.plot(np.linspace(-5, 45, 1000), [-i for i in G_approximation], color='blue')
