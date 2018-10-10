import sqlite3
import sys
sys.path.insert(0, "data")


class Database:
	def __init__(self, bot=None):
		self.bot = bot
		self.conn = None
		self.DB_NAME = "serverinfo.db"
		print("Database is up and running")
		
		
		
		
		
	def check_prefix(self, serverid):
		self.conn = sqlite3.connect(self.DB_NAME)
		sql = "INSERT OR IGNORE INTO serverinfo (serverid, prefix) VALUES(?,0);"
		self.conn.execute(sql, (serverid,))
		sql = "SELECT prefix, serverid FROM serverinfo WHERE serverid = ?"
		params = (serverid,)
		result = self.conn.execute(sql, params)
		output = ''
		for i in result:
			output = output + i[0]
		self.conn.close()
		return output
		
	
	
	def set_prefix(self, serverid, prefix):
		self.conn = sqlite3.connect(self.DB_NAME)
		
		try:
			sql = "INSERT OR IGNORE INTO serverinfo (serverid, prefix) VALUES(?,0);"
			self.conn.execute(sql, (serverid,))
			params = (prefix, serverid,)
			sql = "UPDATE serverinfo SET prefix = ? WHERE serverid = ?;"
			self.conn.execute(sql, params)
			self.conn.commit()
			self.conn.close()
		finally:
			pass
		
		
if __name__ == '__main__':
	db = Database()	