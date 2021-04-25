import sqlite3 as sql

def create_journal():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("create table if not exists journal (timestamp text,entry text not null);")
    con.commit()
    con.close()

def insert_entry(timestamp, entry):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO journal (timestamp, entry) VALUES (?,?)", (timestamp, entry))
    con.commit()
    con.close()

def retrieve_entries():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM journal")
	users = cur.fetchall()
	con.close()
	return users