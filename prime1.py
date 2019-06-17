while True:
	num=int(input("enter any no. more than 2 and less than 7"))
	if num>2 and num<7:
		break;
p,di,j=2,dict(),0
while j<=num:
	prime_check=0
	for i in range(2,p-1):
		if p%i==0:
			prime_check=1
		if prime_check==0:
			di[p]=1
			for i in range(p,1,-1):
				di[p]=di[p]*i
			j+=1
	p+=1
while True:
	pnum=int(input("\n enter the prime no you want factorial of:\n"))
	if pnum in di:
		print(di[pnum])
		break;
	print("this is not a prime no that comes in")