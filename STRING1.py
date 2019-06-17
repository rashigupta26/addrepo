n=int(input("choice"))
di=dict()
for i in range(n):
	v=input("enter string : ")
	if v[0] not in di :
		di[v[0]]=[]
	di[v[0]].append(v)
choice=input("str choice")
if choice in di:
    print(di[choice])
else:
     print("no string starting with"+choice)	