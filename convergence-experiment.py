def f(x):
	if x>=0 and x<1:
		return x
	else:
		return 0
def g(x):
	if x>=0 and x<1:
		return x*x
	else:
		return 0
def h(x):
	return round(x)
#_--------------------------
seq1={}
seq2={}

def printstats():
	global seq1,seq2
	repeats1=max(seq1.values())
	repeats2=max(seq2.values())
	seqq1=[i for i in seq1 if seq1[i]==repeats1]
	seqq2=[i for i in seq2 if seq2[i]==repeats2]
	print("_"*50)
	print("y_n")
	print(list(seq1.items())[:10])
	print("liminf:",min(seqq1))
	print("limsup:",max(seqq1))
	print("-"*50)
	print("y_n/(n+1)")
	print(list(seq2.items())[:10])
	print("liminf:",min(seqq2))
	print("limsup:",max(seqq2))
	print("_"*50)
#----------------------------
def looper(func,a,b,n):
	global seq1, seq2
	for m in range(1,n+1):
		currval=func(a)
		step=(b-a)/m
		for i in range(0,m+1):
			currval+=func(a+i*(step))
		v=round(currval*100)/100
		try:
			seq1[v]+=1
			seq2[round(currval/(n+1)*100)/100]+=1
		except:
			seq1[v]=1
			seq2[round(currval/(n+1)*100)/100]=1
	seq1=dict(sorted(seq1.items(),key=lambda i:-i[1]))
	seq2=dict(sorted(seq2.items(),key=lambda i:-i[1]))
#_---------------------------------------
iters=int(input(" n = "))
while iters!=0:
	looper(f,0,1,iters)
	printstats()
	seq1={}
	seq2={}
	iters=int(input(" n = "))
