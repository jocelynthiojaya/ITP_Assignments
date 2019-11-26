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

#4
def is_member(value: str, list: [str]):
    for i in list:
        if value == i:
            print("True")
            return
        else:
            print("False")
            return
is_member("m", ["a","b","c"])

#5
def is_overlapping(list1: [str], list2: [str]):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


print(is_overlapping(["a","b","c"],["c","d","e"]))

#6
def histogram(list: [int]):
    for i in list:
        print("*" * i)

histogram([3,5,6])