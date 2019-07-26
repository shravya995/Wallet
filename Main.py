from my_functions import *
from Model import User
while True:
	print("-_-"*15)
	print("Choose an option\n----------------------\n1.Login\n2.Register\n3.View Balance\n4.Add Money\n5.Withdraw\n6.Send Money\n7.Show Transactions")
	print("-_-"*15)
	choice=int(input("--> "))
	if choice==1:
		user=login()
	elif choice==2:
		while True:
			print("*"*30,"\n")
			username=input("Enter user name \n--->")
			user = User.select().where(User.user_name==username)

			if len(user)==0:
				fullname=input("Enter full name \n---> ")
				password=input("Enter password \n--->")
				register(fullname,username,password)
				print("*"*30,"\n")

				break
			else:
				print("User_name exists!!")
	elif choice==3:
		user=login()
		if user==0:
			print("login failed")
			continue
		view_balance(user)
	elif choice==4:
		user=login()
		if user==0:
			print("login failed")
			continue
		add_money(user)
	elif choice==5:
		user=login()
		if user==0:
			print("login failed")
			continue
		withdraw(user)
	elif choice==6:
		user=login()
		if user==0:
			print("login failed")
			continue
		send_money(user)
	elif choice==7:
		user=login()
		if user==0:
			print("login failed")
			continue
		show_transactions(user)

	else:
		exit()


