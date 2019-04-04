# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 15:54:48 2018

@author: fWX17106
"""

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
df = pd.read_excel('SA.xlsx')

df['SAtime'].hist(bins=df['SAtime'].max(), density=True, cumulative=True, histtype='step')
df['SAtime'].hist(bins=df['SAtime'].max(), density=True, cumulative=False, histtype='step')

plt.xticks(np.linspace(0, 100, 11, endpoint=True))
plt.yticks(np.linspace(0, 1, 11, endpoint=True))
plt.xlim([0, 100])
plt.ylim([0, 1])
plt.grid(True)
plt.xlabel('SA切换间隔', fontsize='24')
plt.ylabel('CDF/PDF', fontsize='24')

plt.legend(labels=['CDF', 'PDF'], loc=2, fontsize='24')

plt.show()
