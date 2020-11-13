#!/usr/bin/python3.5
#by-Piyus Mohanty
#dt-3/6/18
#to calculate GC % in dna strand
dna=input("enter dna sequence")
count=0
def gc_count(dna,value):
	
	for idx,i in enumerate(dna):
		if i =="G" or i=="C":
			value=value+1
		else:
			idx=idx+1
	print(value)
	l=len(dna)
	pervalue=(value/l)*100
	print("percentage of gc in dna sequence is :")
	print(pervalue)
	
gc_count(dna,count)
