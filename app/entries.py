import sqlite3 as sql

def create_journal():
    con = sql.connect("database.db")
    cur = con.cursor()
    #cur.execute("drop table journal")
    cur.execute("create table if not exists journal (timestamp text,entry text not null, email text);")
    con.commit()
    con.close()

def insert_entry(timestamp, entry, user):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO journal (timestamp, entry, email) VALUES (?,?,?)", (timestamp, entry, user.email))
    con.commit()
    con.close()
    return True

def retrieve_entries(user):
    con = sql.connect("database.db")
    cur = con.cursor()
    email = user.get_email()
    cur.execute("SELECT * from journal where email = (?)", (email,))
    entries = cur.fetchall()
    # for entry in entries:
    #     print(entry)
    con.close()
    return entries