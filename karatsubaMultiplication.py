def multiply(x,y):
		n=len(str(x))
		a=int(x/(10**(n/2)))
		b=x%(10**(n/2))
		c=int(y/(10**(n/2)))
		d=y%(10**(n/2))
		# ac=multiply(a,c)
		# print(ac)
		# bd=multiply(b,d)
		# print(bd)
		# ad_bc=multiply((a+b),(c+d))
		# print(ad_bc)
		# ad_bc=ad_bc-ac-bd
		# print(ad_bc)
		ans= (10**n) * a*c + (10**(n//2)) * ((a*d)+(b*c)) + b*d
		return(ans)


x=int(input())
y=int(input())
print(multiply(x,y))