from numpy import *
import glob

k=10

f=glob.glob('features/*.npy')
v=load(f[0])
v=zeros((len(v),len(f)))
for i in range(len(f)): v[:,i]=load(f[i]).flatten()
x=[]
r=0
for i in range(len(v)):
	l=[]
	for j in range(k):
		r=random.randint(len(v))
		while r==i:
			r=random.randint(len(v))
		l.append(r)	
	x.append(l)	
total_mse=ones(len(x))
old_mse=mean(total_mse)+1
e=0
while mean(total_mse)<old_mse:
	old_mse=mean(total_mse)
	for i in range(len(x)):
		l=list(x[i])
		for j in range(len(x[i])): l.extend(x[x[i][j]])
		l=list(set(filter(lambda a: a!=i,l)))
		mse=zeros(len(l))		
		for j in range(len(l)):	mse[j]=mean((v[i]-v[l[j]])**2)
		sort_mse=argsort(mse)
		del x[i]
		x.insert(i,[])
		for j in range(k): x[i].append(l[sort_mse[j]])
		total_mse[i]=mean(sort(mse)[0:k])
		if random.randint(10000)==0: print e,i,mean(total_mse),old_mse-mean(total_mse)
	print e,i,mean(total_mse),old_mse-mean(total_mse)
	print '---------------------------------------------'
	e+=1
