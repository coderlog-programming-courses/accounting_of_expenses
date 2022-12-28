import sqlite3

conn = sqlite3.connect('contact_information.db')
query = ('''CREATE TABLE CONTACT_INFORMATION(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, USERNAME CHAR(50) NOT NULL, PASSWORD TEXT);''')
conn.execute(query)
conn.close()