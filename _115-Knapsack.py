#prict max val that can be in a knapsack of capacity C
#val is values array and wt is array of weigths
def knapsack(C,wt,val,n):
	k=[[0 for x in range(C+1)]for x in range(n+1)]

	for i in range(n+1):
		for w in range(C+1):
			if i==0 or w==0:
				k[i][w]=0
			elif wt[i-1]<=w:
				k[i][w]=max(val[i-1]+k[i-1][w-wt[i-1]],k[i-1][w])
			else:
				k[i][w]=k[i-1][w]
	return(k[n][C])

val=[60,100,120]
wt=[10,20,30]
C=50
n=len(val)
maxval=knapsack(C,wt,val,n)
print(maxval)
