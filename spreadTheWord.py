t=int(input())
for i in range(t):
	n=int(input())
	a=list(map(int,input().split()))
	sumA,count,k = 1,0,0
	# print(a)
	# print(sumA,count,k)
	while(sumA < n):
		x=0
		for j in range(k,sumA):
			x+=a[j]
		if sumA%2 == 0:
			sumA+=(sumA/2)+x			
		else: 
			sumA+=((sumA+1)/2)+x
		count=count+1
		k+=1
	print(count)
