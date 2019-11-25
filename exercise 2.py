# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:07:03 2019

@author: jocel
"""

#1
def convertToDays():
    x = float(input("Enter hours:"))
    y = float(input("Enter minutes:"))
    z = float(input("Enter seconds:"))
    print(round(getDays(x, y, z), 4))

def getDays(hours, minutes, seconds):
    return (seconds/86400 + minutes/1440 + hours/24)
#def get_input():
    #x = float(input("Enter a number: "))
    #return x

convertToDays()


#2
def calcWeightOnPlanet(weight, gravity = 23.1):
    mass = weight/9.8
    weight = mass*gravity
    print(weight)

calcWeightOnPlanet(120,9.8)
calcWeightOnPlanet(120)
calcWeightOnPlanet(120,23.1)


#3
def numAtoms(mass, atomicWeight = 196.97):
    numberOfAtoms = ((mass * 6.022*10**23)/atomicWeight)
    print(numberOfAtoms)

numAtoms(10)
numAtoms(10, 12.001)
numAtoms(10, 1.008)
# (gr/Mr) = no. atom/avogadro


#4
def calcNewHeight():
    x = float(input("Enter the current width: "))
    y = float(input("Enter the current height: "))
    z = float(input("Enter the desired width: "))
    correspondingHeight = (y/x)*z
    print(correspondingHeight)

calcNewHeight()

#5
def convertTemp():
    x = float(input("Enter a temperature in Fahrenheit:"))
    resultCelcius = (5/9)*(x-32)
    resultKelvin = (5/9)*(x-32) + 273.15
    print("The temperature in Fahrenheit is: ", str(x))
    print("The temperature in Celsius is: ", resultCelcius)
    print("The temperature in Kelvin is: ", resultKelvin)
#def celcius(n):
   # result = (5/9)*(n-32)
    #return(result)
#def kelvin(n):
    #result = (5/9)*(n-32) + 273.15
    #return(result)

convertTemp()

def inc_by_two(x):
    x = x + 2
    return x
x = 10
inc_by_two(x)
print("x = ", x)

def calc_q1(x): 
    q = 4 * x + 1 
    return q 
 
print(calc_q1(5))


#Pembahasan

s = 1
def f():
    global s #ini buat ngebikin s di dalem fungsi global
    print (s)
    s = 2
    print(s)
f()
print(s)


def calc_q4(x): 
    q = 4 * x + 1 
    return q
 
print(calc_q4(5))

x = round(5.76543, 2) #ini func round. round(angka awal, decimal place)
print(x)