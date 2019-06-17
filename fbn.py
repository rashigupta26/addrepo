#fibnoccai series of first n numbers
n=int(input("enter the no. of series"))
i=0
a=1
b=1
while i<=n:
	c=a+b
	a=b
	b=c
	i+=1	
	print(c)
