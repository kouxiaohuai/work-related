# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 08:25:18 2019

@author: kWX596514
"""

import scipy.stats
import math

STD = 8
PL_SLOPE = 3.57
n = 10000
PI = math.pi
EDGE_P = 0.75
SFM = STD * scipy.stats.norm.ppf(EDGE_P)

area_p = 0
for i in range(n):
    p = scipy.stats.norm(0, STD).cdf(SFM + 10 * PL_SLOPE * math.log10(n/(n-i)))
    area_p += ((1-i/n)**2 - (1-(i+1)/n)**2) * p
print(area_p)
