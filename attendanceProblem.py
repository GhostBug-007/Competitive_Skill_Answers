T=int(input())
for case in range(T):
	x,y=map(int,input().split())
	percent=y/x
	if(percent >= 0.75):
		print(0)
	else:
		need=3*x-4*y
		print(need)
