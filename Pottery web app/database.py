import mysql.connector

database = mysql.connector.connect(
    host="localhost", 
    user="root", 
    passwd="105teh3833234",
    database="potter"
)

cur = database.cursor(buffered=True)

def login_handler(instance):
    cur.execute(f"SELECT hash_ FROM userinfo JOIN users ON users.userID = userinfo.userID WHERE email = '{instance.email}'")
    result = cur.fetchone()
    if result:
        if instance.enc_st.hexdigest() == result[0]:
            return True, 'Login Succesful'
        return False, "Email/Password doesn't match."
    

def signup_handler(instance):
    cur.execute('CALL SIGNUP_PROC(%s, %s)', (instance.email, instance.enc_st.hexdigest()))
    return True, 'Sign-up succesful.'


def database_handler(instance):
    '''takes standard parameters, state is type <bool> reference to wether traffic belongs to signup or login.'''

    cur.execute(f"SELECT userID FROM users WHERE email = '{instance.email}'")

    if cur.fetchone():
        if instance.state:
            return login_handler(instance)
        return False, 'Email already in database. Signup Failure.'
    
    else:
        if instance.state:
            return False, 'Email not found. Login Failure'
        return signup_handler(instance)