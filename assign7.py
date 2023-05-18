# Assigmnement 7 

# Sum of All the elements in a list

l = [1,2,3,4,5,23,-23,423,-23]
sum = 0

for i in l:
    sum += i

print(sum)

# largest element in an array 

def man(list):
    max = []
    for i in list:
        max.append(i)
        max.sort(reverse=True)
    print(max[0])     


l = [1,2,3,4,5,23,-23,423,-23]

mnum = man(l)
print(mnum)

# Program to inverse the list

l = [1,2,3,4,5,23,-23,423,-23]

print(l[::-1])

# Program to Split the array at given index and then add the split part to the end 

def splitAdd(l, split):
    '''
    l = list
    split = splitIndex
    '''
    out = []
    for i in range(len(l)):
        index = (i+len(l)+split)%len(l)
        out.append(l[index])
        
    return out

# To check if the given array is monotonic or not

def mono(list):
    temp_list = []

    for i in list:
        temp_list.append(i)
        temp_list.sort()
    
    if list == temp_list:
        print("The given list is monotonic list ")
    else:
        print("The list is not monotonic list")

l = [1,2,3,4,5,6,389,32132,121,12,3]

a = mono(l)

print(a)
