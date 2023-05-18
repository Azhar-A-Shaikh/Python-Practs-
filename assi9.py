### 1. Write a Python program to check if the given number is a Disarium Number?
def is_disarium_number(num):
    num_str = str(num)
    length = len(num_str)
    disarium_sum = 0

    for i in range(length):
        disarium_sum += int(num_str[i]) ** (i + 1)

    if disarium_sum == num:
        return True
    else:
        return False

# Test the function
number = int(input("Enter a number: "))

if is_disarium_number(number):
    print(number, "is a Disarium number")
else:
    print(number, "is not a Disarium number")

### 2. Write a Python program to print all disarium numbers between 1 to 100?

for i in range(1, 101):
    if is_disarium_number(i) == True:
        print(i, end = ' ')

### 3. Program to find if a number is a happy number 

def is_happy_number(num):
    seen_numbers = set()

    while True:
        sum_of_squares = sum(int(digit) ** 2 for digit in str(num))

        if sum_of_squares == 1:
            return True
        elif sum_of_squares in seen_numbers:
            return False
        else:
            seen_numbers.add(sum_of_squares)
            num = sum_of_squares

# Test the function
number = int(input("Enter a number: "))

if is_happy_number(number):
    print(number, "is a Happy number")
else:
    print(number, "is not a Happy number")

### 4. Happy number in range of 1,100 

for i in range(1, 101):
    if is_happy_number(i) == True:
        print(i, end = ' ')

### Find harshad number 
def is_harshad(num):

    temp = num
    total = 0
    while (temp > 0):
        total = total + (temp%10)
        temp = temp//10
        
    if num%total==0:
        print("Harshad Number")
    else:
        print("Not Harshad Number")

### Pronic numbers 

i = 0
while True:
    pronicNum = i*(i+1)
    i = i + 1
    if pronicNum > 100:
        break
    print(pronicNum, end = ' ')
