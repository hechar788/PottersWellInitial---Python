import hashlib
from database import database_handler
from flask import flash, url_for, session
from markupsafe import Markup

class conn:
    '''Initializes user connection object, password encryption happens here.'''
    def __init__(self, email, passwd, state):
        self.email = email 
        self.enc_st = hashlib.sha512(passwd.encode('utf-8'))
        self.state = state  

def handler(email, passwd, state=False): #state True = user login, state False = user sign-up
    '''Creates object with users connection details, passes object to database handler to validate incoming credentials against
    database. Sends user back to correct page if sign-up/login is valid or handles the flash.'''
    connection=conn(email, passwd, state)
    conn_result = database_handler(connection)

    if conn_result[0]:
        if connection.state:
            session['user_id'] = conn_result[2]
            return conn_result[1]

        return conn_result[1]+' Proceed to Login.'

    ##################### flash messages

    if 'Email' in conn_result[1]:
        if not(connection.state):
            flash(Markup(f'''Email already in use, proceed to <a href="{url_for('views.login')}">login</a>'''))
        else:
            flash(Markup(f'Email not found, signup <a href="{url_for('views.sign_up')}">here</a>'))
    else:
        flash(conn_result[1])