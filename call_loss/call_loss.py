# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:16:26 2019

@author: kWX596514
"""

import itertools

pipeNum = 1


def collision(group):
    p_collision = 1
    p_0 = 1
    n = len(group)
    for i in range(n):
        p_0 = p_0 * (1-group[i])
        p_1 = group[i]
        index_1 = list(range(n))
        index_1.remove(i)
        for l in index_1:
            p_1 = p_1 * (1-group[l])
#        print(p_1)
        p_collision = p_collision - p_1
        for j in range(i+1, n):
            p_2 = group[i]*group[j]
            index_2 = list(range(n))
            index_2.remove(i)
            index_2.remove(j)
            for k in index_2:
                p_2 = p_2 * (1-group[k])
#            print(p_2)
            p_collision = p_collision - p_2
#    print(p_0)
    p_collision = p_collision - p_0
    return p_collision


def call_loss(group):
    total_loss = 0
    group_len = len(group)
    group_inverse = [1-i for i in group]
    for num_call in range(group_len+1):
        list_call = list(itertools.combinations(group, num_call))
        list_no_call = list(itertools.combinations(group_inverse, group_len-num_call))
        
        for i in range(len(list_call)):
            conduct_call = 1
            conduct_no_call = 1
            try:
                for j in range(num_call):
                    conduct_call = conduct_call * list_call[i][j]
            except IndexError:
                conduct_call = 1
    
            try:
                for k in range(group_len-num_call):
                    conduct_no_call = conduct_no_call * list_no_call[-1-i][k]
            except IndexError:
                conduct_no_call = 1
            
            loss = conduct_call * conduct_no_call * (num_call-pipeNum) if (num_call-pipeNum) > 0 else 0
            total_loss = total_loss + loss
    return total_loss/sum(group)
