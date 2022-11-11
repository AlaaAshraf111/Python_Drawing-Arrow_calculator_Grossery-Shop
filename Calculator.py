
'''
                 Task_1           3/11/2022
               (Calculator)
'''

print("**************Calculator Program for two numbers******************")
print("For Seintific mode enter 'S'")
print("For Programming mode enter 'P'")
choice=input("enter the mode :")

dicS={"ADD":1,"SUB":2,"DIV":3,"FloorDIV":4}
dicP={"oct":1,"hex":2,"bin":3,"dec":4}




if choice=='S' :
	print("______________________________")
	print("This is the seintific mode")
	print("For addition operation enter 'ADD'")
	print("For subtraction operation enter 'SUB'")
	print("For division operation enter 'DIV'")
	print("For floor-division operation enter 'FloorDiv'")
	
	x =int(input("please enter the first number: "))
	y =int(input("please enter the second number:"))
	z=input("please enter the wanted operation :")
	check=dicS[z]

	if check==1:
		print("x+y %d"%(x+y))
	elif check==2:
		print("x-y %d"%(x-y))
	elif check==3:
		res=x/y
		print("x/y %f"%res)
	elif check==4:
		print("x//y %d"%(x//y))

elif choice=='P':
	print("______________________________")
	print("This is the programming mode")
	print("Choice the format of the number")
	print("For 'oct' enter 'O'")
	print("For 'hexdecimal' enter 'H'")
	print("For 'binary' enter 'B'")
	print("For 'decimal' enter 'D'")
	
	c=input()
	num=input("please enter the number: ")
	if c=='O':
		x =int(num,base=8)
	elif c=='H':
		x =int(num,base=16)
	elif c=='B':
		x =int(num,base=2)	
	elif c=='D':
		x =int(num)
	else:
		print("Wrong choice")
		
	print("Choice the format of the output number")
	print("For getting the oct representation enter 'oct'")
	print("For getting the hex representation enter 'hex'")
	print("For getting the bin representation enter 'bin'")
	print("For getting the dec representation enter 'dec'")
	

	z=input("please enter the wanted operation :")
	check=dicP[z]

	if check==1:
		print("the oct >> "+str(oct(x)))
	elif check==2:
		print("the hex >> "+str(hex(x)))
	elif check==3:
		print("the bin >> "+str(bin(x)))
	elif check==4:
		print("the dec >> "+str(x))
	else: 
		print("Wrong choice")	

	