from Model import User,Wallet,Transaction
from datetime import datetime
def login():
	print("*"*30,"\n")
	user_name=input("Enter username---> ")
	password=input("Enter password----> ")
	try:
		user=User.select().where(User.user_name==user_name).get()

		if user.password==password:
			print("Logged in successfully.\n")
			print("*"*30,"\n")
			return user
		else:
			print("Incorrect password.\n")
			return 0
	except:
		print("Incorrect Credentials")
		return 0
def register(fullname,username,password):

	
	user=User(full_name=fullname,user_name=username,password=password)
	user.save()
	wallet = Wallet.create(customer_id=user)
	transaction=Transaction.create(customer_id=user,timestamp=datetime.now())
	print("Registration complete")
def view_balance(user):
	user1=Wallet.select().where(Wallet.customer_id==user).get()
	print("The balance is:\n--------------------")
	print(user1.balance)
	print("*"*30,"\n")

def add_money(user):
	money=float(input("Enter the amount to be added\n--->"))
	user1=Wallet.select().where(Wallet.customer_id==user).get()
	comments=input("Enter comments\n--------------------------------------\n")
	bal=user1.balance
	bal=bal+money
	entry=Transaction(customer_id=user,transaction_amount=money,type_transaction="Deposit",timestamp=datetime.now(),comments=comments)
	entry.save()
	query = Wallet.update(balance=bal).where(Wallet.customer_id==user)
	n = query.execute()
	print("*"*30,"\n")

def withdraw(user):
	money=float(input("Enter the amount to remove money\n---"))
	user1=Wallet.select().where(Wallet.customer_id==user).get()
	comments=input("Enter comments\n--------------------------------------\n")
	bal=user1.balance

	if bal==0:
		print("YOU'RE BROKE!! ")
		print("*"*30,"\n")
	else:
		bal=bal-money
		entry=Transaction(customer_id=user,transaction_amount=money,type_transaction="Withdraw",timestamp=datetime.now(),comments=comments)
		entry.save()
		query = Wallet.update(balance=bal).where(Wallet.customer_id==user)
		n = query.execute()
		print("*"*30,"\n")
def send_money(user):
	money=float(input("Enter the amount to be sent--->"))
	user1=Wallet.select().where(Wallet.customer_id==user).get()
	comments=input("Enter comments\n--------------------------------------\n")

	bal=user1.balance
	if money>bal :
		print("YOU'RE BROKE!! ")
		print("*"*30,"\n")
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
		entry=Transaction(customer_id=user,transaction_amount=money,type_transaction="Withdraw",timestamp=datetime.now(),comments=comments)
		entry.save()
		entry=Transaction(customer_id=receive_user,transaction_amount=money,type_transaction="Deposit",timestamp=datetime.now(),comments=comments)
		entry.save()
		print("*"*30,"\n")

def show_transactions(user):
	users=Transaction.select().where(Transaction.customer_id==user)
	print("%20s|%20s|%20s|%30s|"%("Transaction Amount","Type of Transaction","Timestamp","comments"))
	print("%60s"%('-'*93))
	for i in users:
		print("%20s|%20s|%20s|%30s|"%(i.transaction_amount,i.type_transaction,i.timestamp,i.comments))
	print("*"*30,"\n")







	# user1=Wallet.select().where(Wallet.customer_id==user)
	# for user2 in user1:
	# 	user2=Wallet.update(balance=user2.balance+money)
		



			
	    
		
	
	