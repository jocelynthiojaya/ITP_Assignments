# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:49:58 2019

@author: jocel
"""
#Exercise 1
inventory = {
 'gold' : 500,
 'pouch' : ['flint', 'twine', 'gemstone'],
 'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

inventory['pocket'] = 'seashell','strange berry','lint'
print(inventory)

inventory['backpack'].sort()
print(inventory)

inventory['backpack'].remove('dagger')
print(inventory)

inventory['gold'] = inventory['gold'] + 50
print(inventory['gold'])

#Exercise 2
prices = {
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}

stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

for i in prices:
    print(i)
    print("price: ", prices[i])
    print("stock: ", stock[i])
    
total = 0
for i in prices: 
    total += prices[i] * stock[i]
print(total)

#Exercise 3
groceries = ['banana', 'orange', 'apple']
def compute_bill(fruit: [str]):
    total = 0
    for i in fruit:
        if stock[i] > 0:
            stock[i] -= 1
            total += prices[i]
    return total

print(compute_bill(groceries))

#Exercise 4
eren = {
 "name": "Eren",
 "homework": [90.0,97.0,75.0,92.0],
 "quizzes": [88.0,40.0,94.0],
 "tests": [75.0,90.0]
}

mikasa = {
"name": "Mikasa",
"homework": [100.0, 92.0, 98.0, 100.0],
"quizzes": [82.0, 83.0, 91.0],
"tests": [89.0, 97.0]
}

armin = {
"name": "Armin",
"homework": [0.0, 87.0, 75.0, 22.0],
"quizzes": [0.0, 75.0, 78.0],
"tests": [100.0, 100.0]
}

students = [eren, mikasa, armin]

#for each student in your students list, print out that student's data, as follows:
for i in students:
    for j in i:
        print(j, ": ", i[j])
    print("")

#Write a function average that takes a list of numbers and returns the average
numbers = [2 , 4, 6]
def average(x: [float]):
    total = sum(x)/len(x)
    return total
print(average(numbers))

#Write a function called get_average that takes a student dictionary
def get_average(student: dict):
    hw = average(student["homework"]) * 0.1
    qz = average(student["quizzes"]) * 0.3
    ts = average(student["tests"]) * 0.6
    return hw + qz + ts

print(get_average(armin))

#Define a new function called get_letter_grade that has one argument called score. 
def get_letter_grade(score: float):
    if 90 <= score:
        print("A")
    elif 80 <= score < 90:
        print("B")
    elif 70 <= score < 80:
        print("C")
    elif 60 <= score < 70:
        print("D")
    else:
        print("F")

get_letter_grade(get_average(eren))
get_letter_grade(get_average(mikasa))
get_letter_grade(get_average(armin))

#Define a function called get_class_average that has one argument, students
def get_class_average(students: list):
    results = []
    for i in students:
        score = get_average(i)
        results.append(score)
    return average(results)

print(get_class_average(students))
get_letter_grade(get_class_average(students))