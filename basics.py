# Python assignment 3

# program to check if number is positive , negaive or zero 

num1 = int(input("Enter a number to check "))

if num1 == 0:
    print("The enteered number is Zero")
elif num1 > 0:
    print("The number is positive")
else:
    print("Number is negative")

# Write a program to check if number is odd or even 

num2 = int(input("Enter a number "))

if num2 %2 == 0:
    print("The entered number is Even ")
else:
    print("The entered number is odd")

# Program to check if the year is a leap year or now 

year = int(input("Enter a year "))

if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
    print('Its a leap year')
else:
    print("its not a leap year")

# Program to check for prime number

def is_prime(num):
    if num <= 1:
        return False

    # Check for divisibility from 2 to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

number = int(input("Enter a number: "))

if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")

# Program to print all the prime numbers between 2 Numbers 

def is_prime(num):
    if num <= 1:
        return False

    # Check for divisibility from 2 to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

# Define the interval
start = 1
end = 10000

print("Prime numbers between", start, "and", end, "are:")

for number in range(start, end + 1):
    if is_prime(number):
        print(number)

        



