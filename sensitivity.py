#!/usr/bin/python3.5
#TP,FP,TN.FN done with reference to training,predictive
#FN-1,0
#FP-0,1
import csv
import math
x=[]
f=open("/home/piyus/Desktop/python/rosalind/training_file.csv")
g=open("/home/piyus/Desktop/python/rosalind/predicted-labels.csv")
csv_f=csv.reader(f,delimiter='\t')
csv_g=list(csv.reader(g))
for row in csv_f:
	x.append(row[19])
#print(len(x))
#print(len(csv_g))
def matching_s(csv_g,x):
	TP=0
	FP=0
	FN=0
	TN=0
	for idx,i in enumerate(x):
		if i!=csv_g[idx][0] and int(i)==0 :
			FP=FP+1
		if i==csv_g[idx][0] and int(i)==0 :
			TN=TN+1


		if i==csv_g[idx][0] and int(i)==1:
			TP=TP+1
		if i!=csv_g[idx][0] and int(i)==1:
			FN=FN+1
	Sensitivity=TP/(TP+FN)
	Specificity=TN/(TN+FP)
	Likelihood=Sensitivity/(1-Specificity)
	PPV=TP/(TP+FP)
	Accuracy=(TP+TN)/(TP+FP+TN+FN)
	MCC_numer=(TP*TN)-(FP*FN)
	MCC_denomi=(TP+FP)*(TP+FN)*(TN+FP)*(TN+FN)
	MCC=MCC_numer/math.sqrt(MCC_denomi)



	
	print("TN is:",TN)
	print("TP is:",TP)    
	print("FP is:",FP)
	print("FN is:",FN)
	print("Sensitivity is:",Sensitivity)
	print("Specificity is:",Specificity)
	print("Likelihood  is: ",Likelihood)
	print("PPV is :",PPV)
	print("Accuracy is :",Accuracy)
	print("MCC is :",MCC)



			

			
	

		


matching_s(csv_g,x)
f.close()
g.close() 