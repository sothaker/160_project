from app import app
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from datetime import datetime
import app.users as userHandler
import app.entries as entryHandler

@app.route("/")
def home():
    userHandler.create_users()
    entryHandler.create_journal()
    return render_template('Landing Page.html')

@app.route("/login", methods =['POST', 'GET'])
def login():
    if request.method=='GET':
        return render_template('Login.html')
    else:
        email = request.form["email"]
        print(email)
        password = request.form["psw"]
        user = userHandler.find_user(email)
        if user and password == user[3]:
            return redirect(url_for('dashboard'))
        else:
            return render_template('Login.html', error="Email or password incorrect.")

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method=='GET':
        return render_template('Sign up Page.html')
    else: 
        name = request.form["name"]
        email = request.form["email"]
        bday = request.form["bday"]
        password = request.form["psw"]
        userHandler.insert_user(name, email, bday, password)
        user_list = userHandler.retrieve_users()
        for user in user_list:
            print(user)
        return render_template('Discover.html')

@app.route("/dashboard")
def dashboard():
    return render_template('Dashboard.html')

@app.route("/breathe")
def breathe():
    return render_template('Breathe.html')

@app.route("/journal", methods =['POST', 'GET'])
def journal():
    if(request.method=='GET'):
        entries = entryHandler.retrieve_entries()
        return render_template('Journal.html', entries = entries)
    else:
        timestamp = datetime.now()
        entry = request.form["entry"]
        if len(entry) > 0:
            entryHandler.insert_entry(timestamp, entry)
        entries = entryHandler.retrieve_entries()
        return render_template('Journal.html', entries=entries)

@app.route("/meditate")
def meditate():
    return render_template('Meditate.html')

@app.route("/discover")
def discover():
    return render_template('Discover.html')
