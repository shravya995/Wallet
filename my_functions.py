from Model import User,Wallet
from datetime import datetime
def login():
	user_name=input("Enter username---> ")
	password=input("Enter password----> ")
	user=User.select().where(User.user_name==user_name).get()
	try:
		if user.password==password:
			print("Logged in successfully.\n")
			return user
		else:
			print("Incorrect password.\n")
			return 0
	except:
		print("Incorrect Credentials")
def register(fullname,username,password):
	
	user=User(full_name=fullname,user_name=username,password=password)
	user.save()
	wallet = Wallet.create(customer_id=user, timestamp=datetime.now())
	print("Registration complete")
def view_balance(user):
	user1=Wallet.select().where(Wallet.customer_id==user).get()
	
	print(user1.balance)

def add_money(user):
	money=float(input("Enter the amount to be added"))
	comments=input("What is this for?")
	user1=Wallet.select().where(Wallet.customer_id==user).get()
	
	bal=user1.balance
	bal=bal+money
	query = Wallet.update(balance=bal).where(Wallet.customer_id==user)
	n = query.execute()
	query = Wallet.update(comments=comments).where(Wallet.customer_id==user)
	n = query.execute()
def withdraw(user):
	money=float(input("Enter the amount to remove money"))
	user1=Wallet.select().where(Wallet.customer_id==user).get()
	print("The balance is:\n--------------------")
	bal=user1.balance
	if bal==0:
		print("YOU'RE BROKE!! ")
	else:
		bal=bal-money
		query = Wallet.update(balance=bal).where(Wallet.customer_id==user)
		n = query.execute()
def send_money(user):
	money=float(input("Enter the amount to be sent--->"))
	user1=Wallet.select().where(Wallet.customer_id==user).get()
	bal=user1.balance
	if money>bal :
		print("YOU'RE BROKE!! ")
	else:
		receiver_username=input("Enter the user name of the receiver--->")
		receive_user=User.select().where(User.user_name==receiver_username).get()
		user2=Wallet.select().where(Wallet.customer_id==receive_user).get()
		bal1=user1.balance-money
		bal2=user2.balance+money
		query1 = Wallet.update(balance=bal1).where(Wallet.customer_id==user)
		n1 = query1.execute()
		query2 = Wallet.update(balance=bal2).where(Wallet.customer_id==receive_user)
		n2 = query2.execute()







	# user1=Wallet.select().where(Wallet.customer_id==user)
	# for user2 in user1:
	# 	user2=Wallet.update(balance=user2.balance+money)
		



			
	    
		
	
	