def anagramCheck(caseNum):
	if(caseNum == 0):
		return 0
	else:
		str1,str2=input().split()
		length1,length2=len(str1),len(str2)
		if( length1 != length2): 
			print("No")
			return anagramCheck(caseNum-1)
		#count=0
		list2=list()		
		for char in str2:
			list2.append(char)
		for char in str1:
			if char in list2:
				list2.remove(char)
		#print(list2)
		if not list2:
			print("YES")
			return anagramCheck(caseNum-1)
		else:
			print("NO")
			return anagramCheck(caseNum-1)

caseNum=int(input())
anagramCheck(caseNum)