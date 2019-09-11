#!/usr/bin/python3.5
cents=int(input("Enter the cents value"))
def conversion(cents):
	pennie=int(25)
	dime=int(10)
	nickel=int(5)
	cent=int(1)
	p_c=0
	d_c=0
	n_c=0
	c_c=0

	while(cents!=0):
		if cents >= pennie :
			p_c=p_c+1
			a=cents-pennie
			#print(a)
			cents=int(a)
	
		elif cents >= dime :
			d_c=d_c+1
			a=cents-dime
			#print(a)
			cents=int(a)
	
		elif cents >= nickel :
			n_c=n_c+1
			a=cents-nickel
			#print(a)
			cents=int(a)
	
		elif cents >= cent :
			c_c=c_c+1
			a=cents-cent
			#print(a)
			cents=int(a)
	if p_c!=0:
		print("no of quarters: ",p_c)
	if d_c!=0:
		print("no of dimes : ",d_c )
	if n_c!=0:
		print("no of nickel: ",n_c)
	if c_c!=0:
		print("no of cents: ",c_c)


    	

	
	
	
	print("Total no of coin are:",(p_c)+(d_c)+(n_c)+(c_c))
   
    
     
    
conversion(cents)
