# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 10:56:59 2019

@author: jocel
"""

#1
def max_(x,y):
    if x > y:
        print(x)
    else:
        print(y)

max_(3,2)

#2
def max_of_three(x,y,z):
    if x > y and x > z:
        print(x)
    elif y > x and y > z:
        print(y)
    else:
        print(z)
        
max_of_three(1,2,8)

#3
def length(arrayName):
    x = 0
    for i in arrayName:
        x = x + 1
    print("The length of the given list is: " + str(x))
    return x

sports = ['basketball', 'soccer', 'badminton']
length(sports)

#4
def vowel(x):
    vowels = ("a", "i", "u", "e", "o")
    for i in vowels:
        if i == x:
            return True
    return False

vowel("k")

#5
def reverse(string):
    return string[::-1]
#[start:end:lompatannya]
    
print(reverse("Bentliy"))
def multiply_list(start, stop): 
    product = 1 
    for element in range(start, stop): 
        product = product * element 
    return product 
x = multiply_list(1, 5)
print(x)

#6
def palindrome(word):
    return (word[::-1] == word[::1])
print(palindrome('sunset'))
print(palindrome('radar'))

#7
def palindrome2(word):
    x = word.replace(" ", "")
    return (x[::-1] == x[::1])
print(palindrome2("go hang a salami im a lasagna hog"))

#8
def generate_n_chars(n:int, c:str):
    print(n*c)
    
generate_n_chars(7,"b")

#9
def calculateScore(score):
    if 0.0 <= score < 0.6:
        print("F")
    elif 0.6 <= score < 0.7:
        print("D")
    elif 0.7 <= score < 0.8:
        print("C")
    elif 0.8 <= score < 0.9:
        print("B")
    elif 0.9 <= score <= 1.0:
        print("A")
    else:
        print("Error")

calculateScore(0.6)
calculateScore(0.89)
calculateScore(0.1)
calculateScore(1.0)

#10
def countPay():
    x = float(input("Enter hours: "))
    y = float(input("Rate: "))

    if x<=40:
        Pay = x*y
        print("Pay: " + str(Pay))
        return
    else:
        Pay = 40*y + (x-40)*1.5*y
        print("Pay: " + str(Pay))
        return

countPay()

#11
def distance_from_zero(number):
    if isinstance (number, int):
        print(abs(number))
    elif isinstance (number, float):
        print(abs(number))
    else:
        print("Nope")
        
distance_from_zero(-5.6)
distance_from_zero(90)
distance_from_zero("what?")

#12
def pigLatin(word: str):
    slicing1 = slice(1)
    firstLetter = word[slicing1]
    slicing2 = slice(1,None,None)
    restOfWord = word[slicing2]
    finalWord = restOfWord + firstLetter + "ay"
    print(finalWord)

pigLatin("phyton")

#notsliced = "Alfamart"
#slicing = slice(1,None,None)
#print(notsliced[slicing])