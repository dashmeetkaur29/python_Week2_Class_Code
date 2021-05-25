# 1. Write a Python program which accepts the radius of a circle from the user and
#    compute the area.

'''
This program will take the radius of a circle as input from user and
display the area of circle accordingly
'''

import math

def calculateArea ():
    print("Welcome to circle area calculator")
    radius = input("Please enter the radius of circle : ")  # Taking input from user
    area = math.pi * math.pow(int(radius), 2) #Calculating area of circle
    print(f'The area of a circle with {radius} radius is {area:.3f}')

