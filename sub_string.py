#!/usr/bin/python3.5
#to find all the distinct sub strings in a string
x=input("enter a string")

#y=set(x)
#c=list(y)
#print(str(c))
#print(y)
#print((len(x)))
#b=set()
def subseq(x):
	b=[]
	for i in range(0,len(x)-1,1):
		for j in range(i,len(x),1):
			a=x[i:j+1]
			b.append(a)
	e=set(b)
	trial=list(e)
	sorted_list = sorted(trial, key=len)
	print("The sub strings are:",sorted_list)
	

	print("The total no of sub strings are:",len(e))


	
	
			
#print(b)
#print(e)

	    
	
	
subseq(x)

