# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:52:52 2019

@author: jocel
"""

a = 2 
b = a + 1 // 2 
c = a + 1.0 // 2 
d = (a + 1) // 2 
e = (a + 1.0) // 2 
f = a + 1 / 2 
g = (a + 1) / 2 
print(a, b, c,d,e,f,g)

hello = "yo" 
world = "dude" 
print(hello, world) 

x = 15 
y = x 
x = 20 
print(y) 

x = 10 
y = 20 
a, b = x + 1, y + 2 
print(a, b) 

z = 13 + 13 // 10



#1
degree=150
radian = degree*3.14/180
print(degree)
print(radian)

def countRad (n):
    rad = n*3.14/180
    print(rad)

countRad(150)

#2
students = [80.0,90.0,66.5]

average = (students[0] + students[1] + students[2])/3
for student in students:
    print(student)
    
print(average)


def countAvg (i,j,k):
    avg = (i+j+k)/3
    print(avg)

countAvg(80.0,90.0,66.5)

#3
class1students = 32
class2students = 45
class3students = 51
class1 = class1students//5
class2 = class2students//7
class3 = class3students//6
print(class1)
print(class2)
print(class3)
print("the number of students in each group in class1 is " + str(class1) + ", in class2 is " + str(class2) + ", in class3 is " + str(class3))
leftover1 = class1students-(class1*5)
leftover2 = class2students-(class2*7)
leftover3 = class3students-(class3*6)
print(leftover1)
print(leftover2)
print(leftover3)
print("the number of students leftover in class1 is " + str(leftover1) + ", in class2 is " + str(leftover2) + ", in class3 is " + str(leftover3))

#4
pi = 3.14
pie_diameter = 55.4 
pie_radius = pie_diameter / 2 
circumference = 2 * pi * pie_radius 
circumference_msg = "Jimmy’s pie has a circumference: "
print(circumference_msg + str(circumference))

#5
velocity = 343
frequency = 256
wavelength = velocity / frequency
print("The speed (m/s): " + str(velocity))
print("The frequency (Hz): " + str(frequency))
print("The speed (m): " + str(wavelength))