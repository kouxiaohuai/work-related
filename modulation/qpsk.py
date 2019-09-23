# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:32:49 2019

@author: kWX596514
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
plt.grid(True)

N = 10000
SINR = 10
R = 1
noisePower = 10**(-SINR/10) * 2*R**2
awgnSigma = (noisePower/2)**0.5

x1, x2, x3, x4 = [], [], [], []
y1, y2, y3, y4 = [], [], [], []
for _ in range(N):
    x1.append(R + awgnSigma*np.random.randn())
    y1.append(R + awgnSigma*np.random.randn())
    x2.append(-R + awgnSigma*np.random.randn())
    y2.append(R + awgnSigma*np.random.randn())
    x3.append(-R + awgnSigma*np.random.randn())
    y3.append(-R + awgnSigma*np.random.randn())
    x4.append(R + awgnSigma*np.random.randn())
    y4.append(-R + awgnSigma*np.random.randn())

plt.scatter(x1, y1, s=1)
plt.scatter(x2, y2, s=1)
plt.scatter(x3, y3, s=1)
plt.scatter(x4, y4, s=1)
