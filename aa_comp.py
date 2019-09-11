#!/usr/bin/python3.5
import sys
sys.stdout = open("aa_neg_1.txt", "w+")

fh=open("/home/piyus/Desktop/python/rosalind/stepik/Project_ML/aa_composition/126_neg_cd60.txt","r")


z=[]
bale=[]
x=[]
seq = []
dictiona = {}
j = 0 
seq_string = ''
for i,line in enumerate(fh):

    if '>' in line:
        header = line
        header = header[:-1]
        j = j + 1
        
    else:
        
    #if the line is only /n then its the break so assign the header and the string to the dictionary 
        if (line == '\n'):
            
            dictiona[j] = [header,seq_string]
            seq_string = seq_string[:-1]
            seq_string=''
            
    #appending the string to bigger string 
        if '\n' in line:
            line = line[:-1]
            seq_string = seq_string  + line
            
            
for k, v in dictiona.items():
    bale.append(v[1])
#print(bale)
print("A,R,N,D,C,Q,E,G,H,I,L,K,M,F,P,S,T,W,Y,V")   

for idx,i in enumerate(bale):
    #f.write(str(i.count("A")/len(i)))
    print(i.count("A")/len(i),",",i.count("R")/len(i),",",i.count("N")/len(i),",",i.count("D")/len(i),",",i.count("C")/len(i),",",i.count("Q")/len(i),",",i.count("E")/len(i),",",i.count("G")/len(i),",",i.count("H")/len(i),",",i.count("I")/len(i),",",i.count("L")/len(i),",",i.count("K")/len(i),",",i.count("M")/len(i),",",i.count("F")/len(i),",",i.count("P")/len(i),",",i.count("S")/len(i),",",i.count("T")/len(i),",",i.count("W")/len(i),",",i.count("Y")/len(i),",",i.count("V")/len(i))
    
    
    
    
    
        
        
