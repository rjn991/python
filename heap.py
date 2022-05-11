# heap sort

def get_data(a,n):
	for i in range(n):
		a.append(random.randint(0,100))

def heapidy(a,n,i):
	if 2*i+1>=n:
		return

	left=2*i+1
	right=2*i+2
