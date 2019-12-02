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

#3
import calendar
x = int(input("Input the year: "))
y = int(input("Input the month: "))

print(calendar.month(x,y))

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

#7
def stringToInt(list: [str]):
    intList: [int] = []
    for i in list:
        intList.append(len(i))
    return intList
print(stringToInt(["asdf","ghj"]))

#8
def find_longest_word(words:[str]):
    length = 0
    for i in words:
        if length < len(i):
            length = len(i)
    return length
print(find_longest_word(["asdf","ghj","okjes"]))

#9
def filter_long_words(words: [str], n:int):
    longerWords = []
    for i in words:
        if len(i) > n:
            longerWords.append(i)
    return longerWords
print(filter_long_words(["asdf","ghj","okjes","oipiop","qwertyu"],4))

#10
def pangram():
    sentence = input("Enter a sentence: ")
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in letters:
        if i not in sentence.lower():
            return False
    return True
pangram()

#11
def char_freq(str):
    freq = {}
    for letter in str:
        if letter in freq.keys():
            freq[letter] += 1
        else:
            freq[letter] = 1
    return freq


print(char_freq("abbabcbdbabdbdbabababcbcbab"))

#12
#def caesarCipher(text:str):
    #letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #for i in text:
        #text.replace(text[1],text[1+4])
    #print(text)
    #print(letters[1])
#print(caesarCipher("hrllo"))

def encrypt(text:str,s:int): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        # ord("a") finds the order of a character, "a"
        if (char.isupper()): 
            result += chr((ord(char) + s - 65) % 26 + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    return result

encrypt("naomi",13)

#second easier way
def caesar_cipher(str,int):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_word = ""
    for x in str:
        next = alphabet.find(x) + int
        if next >= 26:
            next = next-26
        new_letter = alphabet[next]
        #print(new_letter)
        new_word = new_word + new_letter
    return new_word

print(caesar_cipher("na",13))
#13
def makeForms(verb: str):
    list1 = ('o','ch','s','sh','x','z')
    result1 = verb.endswith('y')
    result2 = verb.endswith(list1)
    
    #print(result)
    if result1 == True:
        #print("yes")
        finalWord = (verb.replace(verb[-1],"") + "ies")
        return(finalWord)
    elif result2 == True:
        #print('yes')
        finalWord = (verb + "es")
        return(finalWord)
    else:
        finalWord = (verb + "s")
        return(finalWord)
print(makeForms("cherry"))
print(makeForms("shush"))
print(makeForms("run"))

#14
def makeForming(verb: str):
    list1 = ['be', 'see', 'flee', 'knee']
    result1 = verb.endswith('e')
    result2 = verb.endswith('ie')
    
    #print(result)
    if result2 == True:
        print('yes')
        #finalWord = (verb.replace(verb[-2],"" + "ying")
        #return(finalWord)
    elif result1 == True:
        #print("yes")
        if verb not in list1:
            #print('yes')
            finalWord = (verb.replace(verb[-1],"") + "ing")
            return(finalWord)
        else:
            finalWord = (verb + "ing")
            return(finalWord)
    
    else:
        finalWord = (verb + "ing")
        return(finalWord)

print(makeForming("fade"))
print(makeForming("be"))
print(makeForming("lie"))

