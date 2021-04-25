import sqlite3 as sql

def create_users():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("create table if not exists users (username text not null unique,email text not null unique,birthday text,password text not null);")
    con.commit()
    con.close()

def insert_user(username, email, birthday, password):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,email,birthday,password) VALUES (?,?,?,?)", (username,email, birthday, password))
    con.commit()
    con.close()

def retrieve_users():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM users")
	users = cur.fetchall()
	con.close()
	return users

def find_user(email):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users where email = (?)", (email,))
    user = cur.fetchone()
    con.close()
    return user