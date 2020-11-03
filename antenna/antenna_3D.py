# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:47:45 2020

@author: 10293639
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


df_horizontal = pd.read_csv('antenna_horizontal.csv', header=None)
df_vertical = pd.read_csv('antenna_vertical.csv', header=None)


n = 360
# theta = np.arange(-np.pi*(179/180), np.pi*(181/180), 2*np.pi/360)
antenna_horizontal = df_horizontal[1][:360]
antenna_vertical = df_vertical[1][:360]
antenna_vertical = np.append(antenna_vertical[89:269], antenna_vertical[269])

antenna_horizontal = np.append(antenna_horizontal[179:], antenna_horizontal[:179])
# antenna_vertical = np.append(antenna_vertical[179:], antenna_vertical[:179])

antenna_horizontal = np.append(antenna_horizontal[:], antenna_horizontal[0])
# antenna_vertical = np.append(antenna_vertical[:], antenna_vertical[0])

antenna_horizontal = antenna_horizontal - antenna_horizontal.min()
antenna_vertical = antenna_vertical - antenna_vertical.min()

pattern = antenna_horizontal.reshape(-1, 361) + antenna_vertical.reshape(181, -1)

theta, phi = np.linspace(0, 2 * np.pi, 361), np.linspace(0, np.pi, 181)
THETA, PHI = np.meshgrid(theta, phi)
R = pattern
X = R * np.sin(PHI) * np.sin(THETA)
Y = R * np.sin(PHI) * np.cos(THETA)
Z = R * np.cos(PHI)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')


N_color = 64
jet = plt.cm.get_cmap('jet', N_color)

distance = (X**2 + Y**2 + Z**2) ** 0.5
distance = distance / distance.max()
distance_color = np.zeros((distance.shape[0], distance.shape[1], 4))
for i in range(distance.shape[0]):
    for j in range(distance.shape[1]):
        for k in [i for i in range(N_color)]:
            if distance[i][j] > k/N_color:
                distance_color[i][j] = jet(range(N_color)[k])
# Creating Colormaps in Matplotlib
# https://matplotlib.org/tutorials/colors/colormap-manipulation.html

plot = ax.plot_surface(
    X, Y, Z, rstride=2, cstride=2, facecolors=distance_color,
    linewidth=0, antialiased=False, alpha=0.5)

ax.view_init(elev=15, azim=60)

plt.show()
