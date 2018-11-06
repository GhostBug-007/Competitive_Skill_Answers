T=int(input())
for case in range(T):
	N=int(input())
	A=list(map(int,input().split()))
	B=list(map(int,input().split()))
	sumA,sumB=sum(A),sum(B)
	diff=sumA-sumB
	if diff < 0:
		diff=diff * -1
	for i in range(0)