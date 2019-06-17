#check if a no. is armstrong
num=int(input("enter any number"))
temp=num
sum=0
while temp>0:
	sum=sum+(temp%10)**3
	temp=int(temp/10)
if sum==num:
	print(num,"is an armstrong number")
else:
	print(num,"is not an armstrong number")