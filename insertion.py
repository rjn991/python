import random

def gen_data(a,n):
	for i in range(n):
		x=random.randint(-100,100)
		a.append(x)

def ins_sort(a):	
	for i in range(1,len(a)):
		key=a[i]
		j=i-1
		while j>=0 and key<a[j]:
			a[j+1]=a[j]
			j=j-1
			a[j+1]=key

a=[]
print("Enter the size : ",end="")
n=int(input())
gen_data(a,n)
print("The numbers are : ")
print(a)
ins_sort(a)
print("The sorted numbers are : ")
print(a)
