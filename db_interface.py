import sqlite3

def insert_contact(username, password):
    conn = sqlite3.connect('contact_information.db')
    conn.execute("INSERT INTO CONTACT_INFORMATION (USERNAME, PASSWORD) VALUES('%s', '%s')"%(username, password))
    conn.commit()
    conn.close()
