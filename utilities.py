#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 11:28:28 2022

@author: annajanuszyk
"""
import unicodedata

def punctuation_marks_in_sentence(sentence):
    count = 0
    for s in sentence:
        if unicode.category(s).startswith("P")
            count = count + 1
    return count    


def words_per_sentence(sentence):
    return len(string.split())


def print_punctuation_marks(sentence):
    punct_str = ""
    for s in sentence:
        if unicode.category(s).startswith("P")
            punct_str += s

    return punct_s


def character_position(sentence):
    return sentence.find(char)


def word_count(words):
    counts  = dict()
    words = str.split()
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
            
    return counts
