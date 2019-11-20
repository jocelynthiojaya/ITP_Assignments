# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:20:26 2019

@author: jocel
"""

#PAGE 46
invitees = ["May","Juni","Julie"]

for name in invitees:
    print("You are invited to dinner " + name)
    
#for i in range(len(invitees)):
    #print("You are invited to dinner " + invitees[i])

print("Sadly, " + invitees[1] + " cannot make it")

invitees.remove("Juni")
invitees.append("August")

for name in invitees:
    print("You are invited to dinner " + name)
    
print(invitees[0] + ", " + invitees [1] + ", " + invitees[2] + ", " + "I have found a bigger dining table!")

invitees.insert(0, "Sept")
invitees.insert(2, "Octo")
invitees.append("Novi")
print(invitees)

for name in invitees:
    print("You are invited to dinner for " + name)

print("The dinner table won't arrive in time")

i = 0 
while i<4:
    print("Dinner is cancelled for " + invitees[i])
    i += 1
    
#for i in range(4):
    #print("Dinner is cancelled for " + invitees[i])

for i in range(4):
    print("Sorry " + invitees[0])
    invitees.pop(0)
print(invitees)

for name in invitees:
    print("You are still invited to dinner " + name)

for i in range(2):   
    del invitees[0]
print(invitees)

#PAGE 50
locations = ["London", "Venice", "New York", "Hawaii", "Norway"]
print(locations)
print(sorted(locations))
print(locations)

locations.reverse()
print(locations)
locations.reverse()
print(locations)
print(sorted(locations, reverse=True))
print(locations)

locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)


print(len(locations))
print(len(invitees))