import sqlite3
db = sqlite3.connect("sqlite.db") 
c = db.cursor() 
c.execute(""" CREATE TABLE users( time, month, day, sum, currency, category )""")
db.close()
