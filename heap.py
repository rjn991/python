# heap sort

def get_data(a,n):
	for i in range(n):
		a.append(random.randint(0,100))

def heapidy(a,n,i):
	if 2*i+1>=n:
		return

	left=2*i+1
	right=2*i+2

	lar_child=left

	if right<n:
		if a[right]>a[left]:
			lar_child=right
		
	if a[lar_child]>a[i]:
		a[i],a[large_child]=a[large_child],a[i]
	#parent and child
		heapify(a,n,lar_child)
	#child mode
def 

	
