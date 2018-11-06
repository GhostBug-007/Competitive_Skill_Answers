def SieveOfEratosthenes(n): 
    prime = [1 for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
    	if (prime[p]):
    		for i in range(p * 2, n+1, p): 
    			prime[i] = 0
    	p += 1
    primelist=[]  
    # Add prime numbers to the list 
    for p in range(2, n): 
        if prime[p]: 
           primelist.append(p)
    # print(primelist)
    return(primelist)



numCases=int(input())
# primeList=[]
primeList=SieveOfEratosthenes(200)
# print(len(primeList))
for case in range(numCases):

	num=int(input())

	for i in range(45):
		if (primeList[0]*primeList[i] < num): continue
		reqPrimes=primeList[:i+1]
		break

	# print(reqPrimes)

	length=len(reqPrimes)

	semiPrimes=[]
	for a in range(length-1):
		for b in range(a+1,length):
			if(reqPrimes[a]*reqPrimes[b] < 200):
				semiPrimes.append(reqPrimes[a]*reqPrimes[b])
	semiPrimes.sort()
	# print(semiPrimes)

	i,j=0,len(semiPrimes)-1

	# print(i, j)
	while(i <= j):
		sumSemi=semiPrimes[i]+semiPrimes[j]
		if sumSemi == num:
			print("YES")
			# print(semiPrimes[i],semiPrimes[j])
			break
		elif sumSemi > num:
			j-=1
		elif sumSemi < num:
			i=i+1

	if sumSemi != num:
		print("NO")
	# print(i,j)