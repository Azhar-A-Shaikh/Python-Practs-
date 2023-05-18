# Python assignment 4

# find Factorial of number

def fact(num):
    if num < 0:
        print("The factorial is not defined for negative number")
    elif num == 0:
        print("Factorial is 1")
    else:
        res = 1
        for i in range(1, num+1):
            res = res * i
        return res
    
number = int(input("Enter a number "))

factorial = fact(number)

print(factorial)

# program to display multiplication table

number = int(input("Enter a number for which you want table: "))

for i in range(1,11):
    print("{} x {} = {}".format(i,number,i*number))

# Program to  display fibonacci series 

def fib():
    num = int(input("Enter the number of terms for fibon series: "))
    a = 0
    b = 1

    if num == 0:
        print("Enter a valid number: ")
    elif num == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,num):
            c = a + b
            a = b
            b = c
            print(c)

fib()
        
# Write a Python Program to Check Armstrong Number?

def is_armstrong_number(num):
    # Convert the number to a string to determine its length
    num_str = str(num)
    length = len(num_str)

    # Calculate the sum of the cubes of each digit
    armstrong_sum = 0
    for digit in num_str:
        armstrong_sum += int(digit) ** length

    # Check if the sum is equal to the original number
    if armstrong_sum == num:
        return True
    else:
        return False

# Test the function
number = int(input("Enter a number: "))

if is_armstrong_number(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")

# Armstrong number in a range of 2 numbers 
low = int(input("Enter the lower value of range: "))
high = int(input("Enter the higher value of range: "))

print("\nFrom {} to {} following are the Armstrong Number:".format(low, high), end='\n')
for i in range(low, high+1):
    
    if(is_armstrong_number(i)):
        print(i, end = ' ')

# print sum of all natural numbers

number = int(input("Enter number"))
total_sum = 0

for i in range(1,number+1):
    total_sum = total_sum + i

print("Sum of {} natural number is {}".format(number, total_sum))  
