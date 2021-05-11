from app import app
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from datetime import datetime
import app.users as userHandler
import app.entries as entryHandler
from app.models import User

@app.route("/")
def home():
    global current_user 
    current_user = None
    userHandler.create_users()
    entryHandler.create_journal()
    return render_template('Landing Page.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method=='GET':
        return render_template('Login.html')
    else:
        email = request.form["email"]
        password = request.form["psw"]
        user = userHandler.find_user(email)
        if user and password == user[3]:
            u = User()
            u.set_user(user)
            global current_user
            current_user = u
            return redirect(url_for('dashboard'))
        else:
            return render_template('Login.html', error="Email or password incorrect.")

@app.route("/logout", methods=['GET'])
def logout():
    global current_user
    current_user = None
    return redirect(url_for('home'))

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method=='GET':
        return render_template('Sign up Page.html')
    else: 
        name = request.form["name"]
        email = request.form["email"]
        bday = request.form["bday"]
        password = request.form["psw"]
        success = userHandler.insert_user(name, email, bday, password)
        user_list = userHandler.retrieve_users()
        for user in user_list:
            print(user)
        if success:
            return render_template('Discover.html')
        else:
            return render_template('Sign up Page.html', error="That email is already in use.")

@app.route("/dashboard")
def dashboard():
    if current_user == None:
        return redirect(url_for('home'))
    return render_template('Dashboard.html')

@app.route("/breathe")
def breathe():
    if current_user == None:
        return redirect(url_for('home'))
    return render_template('Breathe.html')

@app.route("/journal", methods =['POST', 'GET'])
def journal():
    if current_user == None:
        return redirect(url_for('home'))
    if(request.method=='GET'):
        #print(current_user)
        entries = entryHandler.retrieve_entries(current_user)
        return render_template('Journal.html', entries = entries)
    else:
        timestamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        entry = request.form["entry"]
        if len(entry) > 0:
            entryHandler.insert_entry(timestamp, entry, current_user)
        entries = entryHandler.retrieve_entries(current_user)
        return render_template('Journal.html', entries=entries)

@app.route("/meditate")
def meditate():
    if current_user == None:
        return redirect(url_for('home'))
    return render_template('Meditate.html')

@app.route("/discover")
def discover():
    if current_user == None:
        return redirect(url_for('home'))
    return render_template('Discover.html')
