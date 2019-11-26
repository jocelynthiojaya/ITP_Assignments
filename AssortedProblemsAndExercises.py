# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:34:45 2019

@author: jocel
"""

#1
sampleData = "3, 5, 7, 23"
sampleData = sampleData.replace(",","") 
newList = sampleData.split()
newTuple = tuple(newList)
print(newList)
print(newTuple)

#2
var_input = "this is fun"
#print(var_input)
vowel_list = ["a","i","u","e","o"," "]
sentence = ""
for vowel in var_input:
   #print(vowel)
    if vowel in vowel_list:
        sentence = sentence + vowel
        #print(vowel)
    else:
        sentence = sentence + vowel + 'o' + vowel


print(sentence)