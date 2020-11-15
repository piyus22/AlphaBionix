#By- Piyus Mohanty
#Download Biopython to execute this
from Bio.Seq import Seq

#create a sequence object
x=input("Enter DNA sequence")
my_seq = Seq(x)

#print out some details about it
print ("seq %s is %i bases long" % (my_seq, len(my_seq)))
print ("reverse complement is %s" % my_seq.reverse_complement())
print ("protein translation is:%s" % my_seq.translate())
