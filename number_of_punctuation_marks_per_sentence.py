#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 11:28:28 2022

@author: annajanuszyk
"""

count = 0;
str = "Good Morning! This is an example.";

for i in range(0, len(str)):
    if str[i] in ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?"):
        count = count + 1;
        
print("Total number of punctuation marks in string: ");
print(count);