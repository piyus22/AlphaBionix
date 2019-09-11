#!/usr/bin/python3.5
#Split entire sequence as per window size and then calculated GC skew 




lines = open('/home/piyus/Desktop/python/rosalind/chr4.fa', "r").read().splitlines()
seq=[]
for idx,row in enumerate(lines):
	if idx!=0:
		seq.append(row)
#print(seq)
k=int(input("sub sequence size"))
karr=""
for row in seq:#concatenating seq on to a growing string i.e karr 
	karr=karr+row
#print(karr)
def extraction(karr,k):
	seq2=""
	count_g=0
	count_c=0
	GC_skew=[]
	final_seq=[]
	var_seq=""
	var=[]
	for idx,i in enumerate(range(0,len(karr),1)):
		seq2=karr[i:i+k]
		if len(seq2)==k:
			final_seq.append(seq2)
			seq3=seq2.upper()
			var.append(idx)

			count_c=seq3.count("C")
			count_g=seq3.count("G")
			#numer=int(count_g-count_c)
			#denom=int(count_g+count_c)
			#print(count_g)
			#print(count_c)
			if count_g==count_c:
				GC_skew.append(0)
			else:
				equate=(count_g-count_c)/(count_g+count_c)
				GC_skew.append(equate)
			#print(seq2)
			#print(GC_skew)
		

		v=dict(zip(var,GC_skew))

	    
		for key, value in v.items():
			print(key,":",value)


	
		

	
	
	

		
	






extraction(karr,k)