s=input()
length=len(s)
s=list(s)
count=0
j=-1
for step in range(length//2):
	if s[step]!= s[j]:
		count+=1
		break
	j-=1
if(count == 0):
	print("YES")
else:
	print("NO")