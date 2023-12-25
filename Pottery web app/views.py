from flask import render_template, Blueprint, request
from handler import handler

views = Blueprint(__name__, 'views')

@views.route('/')
def home():
    return render_template("homepage.html")


@views.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
    
        #runs querys via mysql-connector to write new account to database
        handler(request.form['email'], request.form['password'])

    
    return render_template("sign-up.html")


@views.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        
        #compares posted info to database for validation of (email, passwd) combination
        handler(request.form['email'], request.form['password'], True)
        
    return render_template("login.html")


@views.route('/our-story/<string:blog_id>')
def our_story(blog_id):
    return f"<h1>our-story {blog_id}<h1>"