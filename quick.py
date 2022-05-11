import random
def gen_data(a,n):	
	for i in range(n):
		x=random.randint(0,100)
		a.append(x)

def quick_sort(a,low,high):
	if(low<high):
		pos=partition(a,low,high)
		#print(pos)
		quick_sort(a,low,(pos-1))
		quick_sort(a,pos+1,high)

def partition(a,left,right):
	key=a[left]
	i=left+1
	j=right
	while True:
		while a[i]<key and i<right:
			i=i+1
		while a[j]>key and j>left:
			j=j-1
		if i<j:
			a[i],a[j]=a[j],a[i]
			i=i+1
			j=j-1
		else:
			break
	a[left],a[j]=a[j],a[left]
	return j

a=[]
print("Enter the size : ",end="")
n=int(input())
gen_data(a,n)
print("The numbers are : ")
print(a)
quick_sort(a,0,n-1)
print("The sorted numbers are : ")
print(a)
