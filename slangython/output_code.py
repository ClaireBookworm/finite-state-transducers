a = 1 
b = 1 

if a % 2 == 0 : 
	print( a ) 

for i in range( 100 + 1 ) : 
	c = a + b 
	a = b 
	b = c 
	if a % 2 == 1 : 
		continue 
	print( a ) 
