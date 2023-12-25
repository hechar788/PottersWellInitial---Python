import hashlib
from database import database_handler
from flask import flash

class conn:

    def __init__(self, email, passwd, state):
        self.email = email 
        self.enc_st = hashlib.sha512(passwd.encode('utf-8'))
        self.state = state

def handler(email, passwd, state=False):
    obj = database_handler(conn(email, passwd, state))
    flash(obj[1])