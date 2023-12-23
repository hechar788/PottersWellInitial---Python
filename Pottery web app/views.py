from flask import render_template, Blueprint, request
from database import signup_database_update, database_login
from handler import handle

views = Blueprint(__name__, 'views')

@views.route('/')
def home():
    return render_template("homepage.html")


@views.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
    
        #runs querys via mysql-connector to write new account to database
        info = handle(signup_database_update(request.form['email'], request.form['password']))
        if info:
            return info[0]
    
    return render_template("sign-up.html")


@views.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        #compares posted info to database for validation of (email, passwd) combination
        info = handle((database_login(request.form['email'], request.form['password'])))
        if info:
            return info[0]  

    return render_template("login.html")


@views.route('/our-story')
def our_story():
    return "<h1>our-story<h1>"