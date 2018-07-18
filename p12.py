n,q=input().split()
if n.isdigit() and q.isdigit():
	n=int(n)
	q=int(q)
	z=0
	a=input().split()
	for i in range(0,len(a)):
		if a[i].isdigit():
			z=z+1
	if z==len(a):
		l=[]
		for i in range(0,q):
			v=input().split()
			l.append(v)
		for i in range(0,len(l)):
			r=l[i]
			s=0
			if r[0].isdigit() and r[1].isdigit():
				for i in range(int(r[0])-1,int(r[1])):
					s=s+int(a[i])
				print(s)
			else:
				continue
	else:
		print("invalid")
else:
	print("Invalid")
