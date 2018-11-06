numCases=int(input())
# wordsDic=dict()
right=["j","k"]
left=["d","f"]
for case in range(numCases):
	wordsDic=dict()
	sum=0
	# arrayN=[]
	N=int(input())
	for i in range(N):
		word=input()
		# arrayN
		# wordsDic[word]=[]
		if word in wordsDic.keys():
			wordsDic[word][0]+=1
			x=int(wordsDic[word][1]/(wordsDic[word][0]))
			wordsDic[word][1]+=x
			sum+=x
			# print(wordsDic)
		else:
			wordsDic[word]=[]
			wordsDic[word].append(1)
			arrayWord=list(word)
			wordsDic[word].append(0)
			length=len(arrayWord)
			for i in range(length):
				if(i==0):
					wordsDic[word][1]+=2
				elif (arrayWord[i-1] in left and arrayWord[i] in left) or (arrayWord[i-1] in right and arrayWord[i] in right):
					wordsDic[word][1]+=4
				else:
					wordsDic[word][1]+=2
			sum+=wordsDic[word][1]
			
	print(sum)