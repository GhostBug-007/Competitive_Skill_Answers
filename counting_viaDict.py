line=input("Enter the input statement: ").split()
count=dict()
print(line)
for word in line:
	count[word]=count.get(word,0)+1
print(count)
maxword=None
maxcount=None
for key,value in count.items():
	if maxcount is None or  value>maxcount:
		maxword=key
		maxcount=value
print("MAX: ", maxword,maxcount)