# Assigment 5

# To find lcm of 2 numbers 

def lcm(a,b):

    high = a if a > b else b

    while True:
        if (high %a == 0) and (high%b ==0):
            break
        else:
            high = high + 1

    return high

a = 7
b = 22
print(lcm(a,b))

# Program to find HCF

def hcf(a, b):
    
    low = a if a < b else b
    
    for i in range(1, low+1):
        if (a%i==0) and (b%i==0):
            hcf = i
            
    return hcf

a = 24
b = 122
print(hcf(a,b))

# convert a number into binacry, Octa and Hexa 
def conversion(num):
    print("Binary:      ", bin(num))
    print("Octal:       ", oct(num))
    print("Hexadecimal: ", hex(num))

print(conversion(7))

# Program to find ASCII 
try:
    char = input("Enter a character: ")
    ASCII = ord(char)
    print("ASCII value of {} is {}".format(char, ASCII))
except Exception as e:
    print(e)

# program to make calculator 

try:
    
    while True:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        print("\nFor addition:       +")
        print("For subtraction:    -")
        print("For multiplicaton:  *")
        print("For division:       /")
        print("For Exit:            X")
        
        ch = input("\nEnter the choice for mathematical operations: ")
         
        if ch == '+':
            output = num1 + num2
        elif ch == '-':
            output = num1 - num2
        elif ch == '*':
            output = num1 * num2
        elif ch == '/':
            output = num1 / num2
        
        if ch == 'X' or ch == 'x':
            break
            
        print("\nResult: ", output)
        
except Exception as e:
    print(e)
