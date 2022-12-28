import sqlite3

def insert_contact(name, username, password):
    conn = sqlite3.connect('contact_information.db')
    conn.execute('INSERT INTO CONTACT_INFORMATION (NAME, USERNAME, PASSWORD) VALUES(?, ?, ?)', (name, username, password))
    conn.commit()
    conn.close()

def retrieve_contacts():
    results = []
    conn = sqlite3.connect('contact_information.db')
    cursor = conn.execute("SELECT name, username, password from CONTACT_INFORMATION")
    for row in cursor:
        result.append(list(row))
    return results