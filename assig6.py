# Program to display fibonacci series using recussion

def fibo(a,b,c):
    if c > 0:
        c -= 1
        print(a, end=' ')
        temp = b
        b = a + b
        a = temp
        fibo(a,b,c)
print(fibo(0,1,10))

# Program to find factorial using recussion 

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

# Program To calculate BMI

def bmi(height, weight):
    
    return weight/(height*height)

bmi(1.8, 70)

# Program to find log of e

import math

try:
    num = int(input("Enter the number: "))
except Exception as e:
    print(e)
else:
    print(math.log(num))

# Cube sum of natural number 

def cubN(n):
    return sum(range(n+1))**3

cubN(3)























