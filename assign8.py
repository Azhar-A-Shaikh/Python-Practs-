# Assigment 8

# Create a program to add 2 matrix

mat1 = [[1,2,3],
        [6, -4, -9],
        [3,6,9]]

mat2 = [[6,9,3],
        [1,-1,1],
        [0, 9, 11]]

result = []

for i in range(len(mat1)):
    row = []
    for j in range(len(mat1)):
        row.append(mat1[i][j]+ mat2[i][j])

    result.append(row)

print(result)

# Program to multily matrix 
# Take 3x3 matrix
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]

# Take a 3x4 matrix

B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]

result = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for r in result:
    print(r)

# program to transpose matrix 

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterating through rows
for i in range(len(X)):
   # iterating through columns
   for j in range(len(X[0])):
        result[j][i] = X[i][j]

for r in result:
    print(r)

# programt to sort a sentence / String 

try:
    sentance = input("Enter the words: ")
    words = [word.lower() for word in sentance.split()]
    words.sort()
    
    print("Sorted order of words:")
    for word in words:
        print(word, end = ' ')
    
except Exception as e:
    print(e)

# Remove punc from a string 

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

string = input("Enter the string: ")

outputString = ""

for char in string:
    if char not in punctuations:
        outputString += char
        
print(outputString)
