def carparfait(x):
	for i in range(x):
		a=(i+1)**2
		if a==x:
			return 0
	return 1

def C(a,b):
	k=0
	for i in range(a-1,b):
		if carparfait(i+1)==0:
			k=k+1
		for j in range(i-1,b):
			if carparfait((i+1)*(j+1))==0:
				k=k+1
			for t in range(j-1,b):
				if carparfait((i+1)*(j+1)*(t+1))==0:
					k=k+1
	return k

print(C(5,10))
		



