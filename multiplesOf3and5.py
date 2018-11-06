sum=0
for num in range(0,1000,1):
	if(num%3 == 0):
		sum+=num
		# print(num)
	elif num%5 == 0:
		sum+=num
		# print(num)
print(sum)