from peewee import *
db = SqliteDatabase('wallet.db')

class User(Model):
	full_name = CharField()
	user_name = CharField()
	password  =CharField()

	class Meta:
		database = db 

class Wallet(Model):
	customer_id = ForeignKeyField(User, backref='entries')
	balance= DoubleField(default=0)

	class Meta:
		database = db
class Transaction(Model):
	customer_id = ForeignKeyField(User, backref='entries')
	transaction_amount=DoubleField(default=0)
	type_transaction=CharField(default="---")
	timestamp=TimestampField()
	comments=TextField(default="---")

	class Meta:
		database = db
if __name__=='__main__':
	
	db.connect()
	db.create_tables([User,Wallet,Transaction])