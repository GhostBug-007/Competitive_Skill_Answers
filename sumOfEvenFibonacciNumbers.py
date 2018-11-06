array=[]
array.append(1)
array.append(2)
num=2
sum=0

# for i in
while(num<4000000):
	if num%2 == 0:
		sum+=num
	num=array[1]+array[0]
	array.remove(array[0])
	array.append(num)
	
	# i=i+1
	# print(num)
print("\n\nThis program prints the sum of all the even terms\nin the fibonacci sequence when the term is less than 4*10^6")
print()
print(sum)
