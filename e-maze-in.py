'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
str=input()
array=[]
for char in str:
    array.append(char)
print(array)
position=[0,0]
length=len(str)
for pos in range(length):
    if(array[pos]=='L'):
        position[0]-=1
    elif(array[pos] == 'R'):
        position[0]+=1
    elif(array[pos] == 'U'):
        position[1]+=1
    elif(array[pos] == 'D'):
        position[1]-=1
    print(position)
print(position[0],position[1])