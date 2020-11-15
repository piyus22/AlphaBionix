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
