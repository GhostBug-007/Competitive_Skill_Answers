numCases=int(input())
# cases=[2010,2015,2016,2017,2019]
for case in range(numCases):
	N=int(input())
	# if(N in cases):
	# 	print("HOSTED")
	# else:
	# 	print("NOT HOSTED")
	if(N == 2010 or N == 2015 or N == 2016 or N == 2017 or N == 2019):
		print("HOSTED")
	else:
		print("NOT HOSTED")
