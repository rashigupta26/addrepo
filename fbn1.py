#fibonacci series offirst n prime numbers
n=int(input("enter the no of series"))
a=1
b=1
i=0
while i<=n:	
	c=a+b
	a=b
	b=c
	prime_check=0	
	
	if c==2:
		print (c)
		i+=1
		continue
	for j in range(2,c): 
		if c%j==0:
			prime_check=1
	if prime_check==0:
		print(c)
		i+=1