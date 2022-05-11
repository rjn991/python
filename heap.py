import random
def gen_data(a,n):
	for i in range(n):
		x=random.randint(0,100)
		a.append(x)
def heapify(a,n,i):
	if 2*i+1>=n:
		return
	left=2*i+1
	right=2*i+2
	lar_child=left
	if right<n:
		if a[right]>a[left]:
			lar_child=right
	if a[lar_child]>a[i]:
		a[i],a[lar_child]=a[lar_child],a[i]
		heapify(a,n,lar_child)
def heap_sort(a):
	n=len(a)
	for i in range(n,-1,-1):
		heapify(a,n,i)
	for i in range(n-1,0,-1):
		a[i],a[0]=a[0],a[i]
		heapify(a,i,0)
a=[ ]
print("enter size: ")
n=int(input())
gen_data(a,n)
print("the numbers are: ")
print(a)
heap_sort(a)
print("the sorted numbers are: ")
print(a)
