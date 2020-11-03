# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:09:44 2020

@author: 10293639
"""

import scipy
import math


precision = 10 ** -6
rate = 0.1
area_coverage_probability = 0.9
shadow_fading_std = 10
base_station_height = 25
propagation_model = 'UMa'
path_loss_slop = 43.42 - 3.1*math.log10(base_station_height)

shadow_fading_margin = shadow_fading_std

a = -shadow_fading_margin/(shadow_fading_std*math.sqrt(2))
b = path_loss_slop*math.log10(math.e)/(shadow_fading_std*math.sqrt(2))
area_coverage_probability_calculate = 0.5*(1 + math.erf(-a) + math.exp((1-2*a*b)/(b**2))*(1-math.erf((1-a*b)/b)))

while abs(area_coverage_probability_calculate - area_coverage_probability) > precision:
    if (area_coverage_probability_calculate - area_coverage_probability) > 0:
        shadow_fading_margin = (1 - rate) * shadow_fading_margin
        a = -shadow_fading_margin/(shadow_fading_std*math.sqrt(2))
        b = path_loss_slop*math.log10(math.e)/(shadow_fading_std*math.sqrt(2))
        area_coverage_probability_calculate = 0.5*(1 + math.erf(-a) + math.exp((1-2*a*b)/(b**2))*(1-math.erf((1-a*b)/b)))
    if (area_coverage_probability_calculate - area_coverage_probability) < 0:
        shadow_fading_margin = (1 + rate) * shadow_fading_margin
        a = -shadow_fading_margin/(shadow_fading_std*math.sqrt(2))
        b = path_loss_slop*math.log10(math.e)/(shadow_fading_std*math.sqrt(2))
        area_coverage_probability_calculate = 0.5*(1 + math.erf(-a) + math.exp((1-2*a*b)/(b**2))*(1-math.erf((1-a*b)/b)))

edge_coverage_probability = scipy.stats.norm(0, shadow_fading_std).cdf(shadow_fading_margin)
handover_gain = (scipy.stats.norm(0, shadow_fading_std).ppf(edge_coverage_probability) - scipy.stats.norm(0, shadow_fading_std).ppf(1-(1-edge_coverage_probability)**0.5))**0.5 * (1.6-(8-shadow_fading_std)/10) - 0.5
print(f'{shadow_fading_margin:.2f}')
print(f'{handover_gain:.2f}')
