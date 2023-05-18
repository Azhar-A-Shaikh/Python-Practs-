# Python assignment 2

# Program to convert kilometer to miles

kilo = 25
miles = 25 / 1.60
print(miles)

# convert celcius to frank

cels = 25
frank = (9*cels/ 5) + 32
print(frank)

# write a program to display calender 
import calendar

year = 2023
month = 5
print(calendar.month(year,month))

# Write a program to solve quadratic equation 

import math

a = int(input(("Enter the coeff a: ")))
b = int(input(("Enter the coeff b: ")))
c = int(input(("Enter the constant c: ")))

d = (b**2) - (4*a*c)

root1 = ((-1*b)+(math.sqrt(d))) / (2*a)
root2 = ((-1*b)-(math.sqrt(d))) / (2*a)

print('\nFor quad eq. {}x^2 + ({})x^1 + {}'.format(a,b,c))
print('The solutions are: {} and {}'.format(root1, root2))

# Swap 2 number without using temp

num1 = 2
num2 = 4

print("Numbers before swap num1 = {} and num2 = {}".format(num1,num2))

num2 = num2 + num1
num1 = num2 - num1 
num2 = num2 - num1

print("Numbers after swap num1 = {} and num2 = {}".format(num1,num2))

