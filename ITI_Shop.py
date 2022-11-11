'''
                   Task_3                  3/11/2022
'''

# Welcome to ITI shop

product ={'Apple':40,'banana':30,'cherry':70}
dic_cost = {'Apple':15,'banana':20,'cherry':30}
customer_choice=[0,0,0]
cost=[0,0,0]

while 1:
	print("______________________________________________________")
	print("#Welcome to ITI Shop")

	print("For customer mode press: 1 \\\ ",end='')
	print("For owner mode press: 2 \\\ ",end='')
	print("For exist press: 0 ")

	x=int(input("please enter the mode:"))

	while x == 1 :    ##Customer Mode
		print("-------------------------")
		print("Customer Mode")
		
		print("To show our products press 1")
		print("To Buy from our products press 2")
		print("to print the bill press 3")	
		print("For exist press: 0 ")	
		
		y=int(input())
		
		if y==1:    #Showing products 
		
			print ("products>>",end='')
			print(list(product),end='')
			print (list(product.values()))
		
		elif y==2:  #Buying products
		
			print("please enter the correct name of product you want")
			p=input()
			print ("enter the quantity")
			q=int(input())
			i=0
			for v in product.keys():
				if p== v:
					if q<=product[v]:
						product[v] -= q
						customer_choice[i] +=q
						cost[i] += q*(dic_cost[v])
				i+=1
				
		elif y==3:  #Printing the bill
		
			print ("the quantity you took from: ")
			print(list(product),end=' ')
			print (customer_choice)
			print("cost= ",end=' ')
			print(cost)

		elif y==0:   #Exist and reset the bill for new operation
			customer_choice[:] = [0 for _ in customer_choice]
			cost[:] = [0 for _ in cost]
			break


	while x == 2 :     ##Owner Mode
		print("-------------------------")
		print("Owner Mode")
		
		print("To Add products press 1")
		print("To show products press 2")
		print("to change cost press 3")	
		print("For exist press: 0 ")	
		
		y=int(input())
		
		if y==1:    #Adding products and it quantity and its cost
		
			print("please enter the name of product you want to add")
			p=input()
			print ("enter the quantity of it")
			q=int(input())
			product[p]=q
			print ("enter the its cost")
			c=int(input())
			dic_cost[p]=c
			customer_choice.append(0)
			cost.append(0)
			print ("products>>",end='')
			print(list(product),end='')
			print (list(product.values()))
			print(dic_cost)
			
		elif y==2:   #Showing products
		
			print ("products>>",end='')
			print(list(product),end='')
			print (list(product.values()))
			
		elif y==3:  #Changing cost
		
			print("please enter the name of product you want to chang its cost")
			p=input()
			print ("enter the new cost")
			q=int(input())
			dic_cost[p]=q
			print ("products>>",end='')
			print(list(product),end='')
			print (list(product.values()))
			print(dic_cost)
			
		elif y==0:
			break
	
