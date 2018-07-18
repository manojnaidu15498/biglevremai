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
		x=[]
		for i in range(0,q):
			d=input().split()
			l.append(d)
		for i in range(0,len(l)):
			r=l[i]
			s=0
			if r[0].isdigit() and r[1].isdigit():
				for i in range(int(r[0])-1,int(r[1])):
					x.append(int(a[i]))
				for j in range(0,len(x)-1):
					xor=x[j+1]^x[j]
					x[j+1]=xor
				print(xor)
				x=[]
			else:
				continue
	else:
		print("invalid")
else:
	print("Invalid")
