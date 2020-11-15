#!/usr/bin/python3.5
#By-Piyus Mohanty
dna=input("enter dna sequence")
motif=input("enter motif to find")#Motif pattern to be found

def motif_find(dna,motif):
	lista=[]
	count=0
	num=len(motif)
	for i in range(0,len(dna),1):
		if dna[i]==motif[0]:
			if dna[i:i+num]==motif:
				count=count+1
				lista.append(i)
				
			
				
	print("no of motif repeats:%d"%(count))
	print(lista)
motif_find(dna,motif)


#!/usr/bin/python3.5
#Alternative for the same, using different approach
import re
seq=input("Enter DNA sequence")
pattern=input("Enter motif to be searched ")
def motif_search(seq,pattern):
	pos=re.finditer(pattern,seq)
	for val in pos:
		print(val)
motif_search(seq,pattern)

