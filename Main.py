from my_functions import *
from Model import User
while True:
	print("Choose an option\n1.Login\n2.Register\n3.View Balance\n4.Add Money\n5.Withdraw\n")
	choice=int(input("--> "))
	if choice==1:
		user=login()
	elif choice==2:
		fullname=input("Enter full name ---> ")
		username=input("Enter user name --->")
		password=input("Enter password --->")
		availability=True
		user = User.select().where(User.user_name==username)

		if len(user)==0:
		#or we can use ' if user.exists():'
			register(fullname,username,password)
		else:
			print("User_name exists!!")
	elif choice==3:
		user=login()
		view_balance(user)
	elif choice==4:
		user=login()
		add_money(user)
	elif choice==5:
		user=login()
		withdraw(user)
	else:
		exit()


