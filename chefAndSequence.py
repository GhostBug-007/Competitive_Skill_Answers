numCases=int(input())
for case in range(numCases):
	N,K=map(int,input().split())
	A=list(map(int,input().split()))
	# print(A)
	sumA=sum(A)
	# print(sumA)
	A.sort()
	# print(A)
	for i in range(1,K+1):
		A[-i]=1
	# print(A)
	# sumA=sum(A)
	for i in range(N):
		A[i]=A[i]*A[i]
	# print(A)
	sSqA=sum(A)
	# print(sSqA, sumA)
	if(sSqA <= sumA):
		print("YES")
	else:
		print("NO")


