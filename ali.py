tag=input()
#print(tag)
code=list()
length=len(tag)
#print(length)
vowels=['A','E','I','O','U','Y']
for i in range(length):
	code.append(tag[i])
#print(code)
for i in range(length):
	if i == 2 or i == 6: continue
	code[i]=int(code[i])
#print(code)
count=0
for i in range(length-1):
	if( i == 1 or i == 2 or i ==5 or i == 6): continue
	if (code[i]+code[i+1]) % 2 != 0 :
		print("invalid")
		count+=1
		break
if code[2] in vowels:
	count+=1
if count == 0:
	print("valid")