


while True:
	opc = int( input("1)suma 2)resta 3)mult 4)div 5)mod 6)SALIR...") )
	
	if opc != 6:
		a = int( input("Ingresa el valor de A: ") )
		b = int( input("Ingresa el valor de B: ") )

	if opc == 1:
		print str(a)+" + "+str(b)+" = "+str(a+b)
	elif opc == 2:
		print str(a)+" - "+str(b)+" = "+str(a-b)
		
	elif opc == 3:
		print str(a)+" * "+str(b)+" = "+str(a*b)
			
	elif opc == 4:
		print str(a)+" / "+str(b)+" = "+str(a/b)
			
	elif opc == 5:
		print str(a)+" % "+str(b)+" = "+str(a%b)
			
	elif opc == 6:
		break							