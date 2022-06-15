#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 11:23:13 2022

@author: annajanuszyk
"""

def word_count(str):
    counts  = dict()
    words = str.split()
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
            
    return counts

print(word_count('This string is an example,'))
