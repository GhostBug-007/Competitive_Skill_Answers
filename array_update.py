N=int(input())
A=input().split()
#print(A)
length=len(A)
#print(length)
for i in range(length):
	A[i]=int(A[i])
#print(A)
x=int(sum(A)/N) + 1
print(x)
for i in range(length):
	A[i]=x
print(A)
