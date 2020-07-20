import sqlite3

# create connection
class DB:
	"""docstring for DB"""
	def __init__(self):
		self.database = 'tablescore.db'

	def connect(self):
		
		self.conn = sqlite3.connect('tablescore.db')
		# create a cursor
		self.c = self.conn.cursor()

	def close_connection(self):
		# close connection
		self.conn.commit()
		self.conn.close()

	def add_record(self, score):
		self.c.execute("INSERT INTO players VALUES (?,?)", ('Adam', score))

		# see the records
	def get_records(self):
		return self.c.execute("SELECT * FROM players")

		#print(self.c.fetchall())
		# Commit our command

		#print('Command executed successfully!')
