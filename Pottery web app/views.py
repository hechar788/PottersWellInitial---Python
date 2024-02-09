from flask import render_template, Blueprint, request, flash, session
from handler import handler

views = Blueprint(__name__, 'views')

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        session.clear()
        return render_template('index.html')

    return render_template('profile.html')


@views.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        #runs querys via mysql-connector to write new account to database
        result = handler(request.form['email'], request.form['password'])
        if result:
            flash(result)
            return render_template('login.html')
    return render_template("sign-up.html")

@views.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        #compares posted info to database for validation of (email, passwd) combination
        result = handler(request.form['email'], request.form['password'], True)
        if result:
            flash(result)
            return render_template('index.html')
    return render_template("login.html")

@views.route('/store')
def store():
    return render_template("store.html")

@views.route('/our-story/<string:blog_id>')
def our_story(blog_id):
    return f"<h1>our-story {blog_id}<h1>"

@views.route('/book_a_class')
def book_a_class():
    return render_template('booking.html')

@views.app_errorhandler(404)
def bad_path(err):
    '''Bad route handler, will return an html template informing the user and automatically redirect them
    back to the home page.'''
    return render_template('bad_url_path.html')