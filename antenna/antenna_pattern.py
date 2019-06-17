# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 13:34:37 2019

@author: kWX596514
"""


import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd


file = 'antenna_pattern.xlsx'
df_h = pd.read_excel(file, sheet_name='Horizontal')
df_v = pd.read_excel(file, sheet_name='Vertical')

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
theta = np.linspace(0, 2*np.pi, 360, endpoint=True)
phi = np.linspace(0, 2*np.pi, 360, endpoint=True)
THETA, PHI = np.meshgrid(theta, phi)
a = df_h['Horizontal_reverse'].values
b = df_v['Vertical_reverse'].values
r = np.outer(a, b)
x = r * np.sin(THETA) * np.cos(PHI)
y = r * np.sin(THETA) * np.sin(PHI)
z = r * np.cos(THETA)

# Plot the surface.
surf = ax.plot_surface(x, y, z, cmap=cm.rainbow,
                       linewidth=0, antialiased=False, alpha=0.5)

# Customize the z axis.
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
