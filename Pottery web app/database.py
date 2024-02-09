import mysql.connector

database = mysql.connector.connect(
    host="localhost", 
    user="root", 
    passwd="105teh3833234",
    database="potter"
)

cur = database.cursor(buffered=True)

def login_handler():
    cur.execute(f"SELECT users.userID FROM userinfo JOIN users ON users.userID = userinfo.userID WHERE email = '{user.email}' AND hash_ = '{user.enc_st.hexdigest()}'")
    result = cur.fetchone()
    if result:
        return True, 'Login Succesful', result[0]
    return False, "Credentials dont match."
    

def signup_handler():
    '''runs database stored procedure for valid signup case.'''
    cur.callproc('SIGNUP_PROCEDURE', (user.email, user.enc_st.hexdigest()))
    database.commit()
    return True, 'Sign-up succesful.'


def database_handler(instance):
    '''takes standard parameters, state is type <bool> reference to wether traffic belongs to signup or login.'''
    global user
    user = instance

    cur.execute(f"SELECT userID FROM users WHERE email = '{user.email}'")

    if cur.fetchone():
        if user.state:
            return login_handler()
        return False, 'Email already in use. Signup Failure.'
    
    else:
        if user.state:
            return False, 'Email not found. Login Failure'
        return signup_handler()