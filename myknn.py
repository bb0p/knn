from numpy import *
import glob
f=glob.glob('features/*.npy')
v=load(f[0])
v=zeros((len(v),len(f)))
for i in range(len(f)):
	v[:,i]=load(f[i]).flatten()
x=[]
r=0
for i in range(len(v)):
	l=[]
	for j in range(10):
		r=random.randint(len(v))
		while r==i:
			r=random.randint(len(v))
		l.append(r)	
	x.append(l)	
for epoch in range(10):
	oldc=10000000
	c=oldc-1
	while c<oldc:
		s=0
		oldc=c
		c=0
		for i in range(len(x)):
			l=[]
			for j in range(len(x[i])):
				l.extend(x[x[i][j]])
			l=list(sorted(set(l)))
				
			j=0
			while j<len(l):
				if l[j]==i: 
					l.pop(j)
				else:
					j+=1
			old=sum((v[i]-v[x[i][epoch]])**2)
			new=0
			newj=i
			for j in range(len(l)):
				new=mean((v[i]-v[l[j]])**2)
				if new<old:
					old=new
					newj=j
			x[i].pop()
			if newj<>i:
				x[i].insert(epoch,l[newj])
				c+=1
			s+=mean((v[i]-v[l[newj]])**2)
		print epoch,s/i,c,oldc
