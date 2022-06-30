#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 11:28:28 2022

@author: annajanuszyk
"""
import unicodedata
import string


def punctuation_count(sentence):
    count = 0
    for i, s in enumerate(sentence):
        # Pause in Chinese requires two charcters
        if unicodedata.category(s).startswith("P"):
            if i > 0 and sentence[i-1] != s:
                count = count + 1
    return count    


def words_per_sentence(text):
    # won't work with Chinese
    sentences = text.split(".")
    result = []
    for sentence in sentences:
        if sentence:
            new_sentence = sentence.strip()
            print(new_sentence.split(" "))
            result.append(len(new_sentence.split(" ")))
    return result


def print_punctuation_marks(sentence):
    punct_str = ""
    for s in sentence:
        if unicode.category(s).startswith("P"):
            punct_str += s

    return punct_s


def character_position(sentence):
    return sentence.find(char)


def word_count(old_sentence):
    # won't work with Chinese
    counts  = dict()
    sentence = old_sentence.translate(str.maketrans("", "",
                                                    string.punctuation))
    words = sentence.split()
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
            
    return counts
