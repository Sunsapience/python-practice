# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 19:59:36 2017

"""
import re

fin = open('test.txt', 'r')

str = fin.read()
str=str.lower()

reObj = re.compile('\b?(\w+)\b?')
words = reObj.findall(str)

wordDict = {}

for word in words:
    
    if word in wordDict:
        wordDict[word] += 1
    else:
        wordDict[word] = 1

for key, value in wordDict.items():
    print('%s: %s' % (key, value))
