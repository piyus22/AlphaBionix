#! /usr/bin/python3
#by-Piyus Mohanty
#Dt-15/9/18
#Find consensus Sequence for an evolutionary block
import numpy as np
seq1=list(input("Enter a sequence of length 5 all in CAPS "))
seq2=list(input("Enter a sequence of length 5 all in CAPS "))
seq3=list(input("Enter a sequence of length 5 all in CAPS "))
seq4=list(input("Enter a sequence of length 5 all in CAPS "))
seq5=list(input("Enter a sequence of length 5 all in CAPS "))
seq=seq1+seq2+seq3+seq4+seq5
array=np.array(seq).reshape(5,5)
print(array)
l1=array[0: ,0:1]
l2=array[0: ,1:2]
l3=array[0: ,2:3]
l4=array[0: ,3:4]
l5=array[0: ,4: ]
unique1, counts = np.unique(l1, return_counts=True)
a=dict(zip(unique1, counts))
unique2, counts = np.unique(l2, return_counts=True)
b=dict(zip(unique2, counts))
unique3, counts = np.unique(l3, return_counts=True)
c=dict(zip(unique3, counts))
unique4, counts = np.unique(l4, return_counts=True)
d=dict(zip(unique4, counts))
unique5, counts = np.unique(l5, return_counts=True)
e=dict(zip(unique5, counts))
import operator
a1=max(a.items(), key=operator.itemgetter(1))[0]
b1=max(b.items(), key=operator.itemgetter(1))[0]
c1=max(c.items(), key=operator.itemgetter(1))[0]
d1=max(d.items(), key=operator.itemgetter(1))[0]
e1=max(e.items(), key=operator.itemgetter(1))[0]
string=a1+b1+c1+d1+e1
print(string)
