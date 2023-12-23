import mysql.connector

database = mysql.connector.connect(
    host="localhost", 
    user="root", 
    passwd="105teh3833234",
    database="potter"
)

cursor = database.cursor(buffered=True)


def signup_database_update(email, passwd): 
    '''database signup function called when users create an account,
        calls 'signup_proc' stored procedure after checking email validity.'''
    
    cursor.execute(f"SELECT email from users WHERE email = '{email}'")
    if cursor.fetchall():
        return False, 'Email already in database. Try again.', 0
    
    cursor.execute(f"CALL signup_proc('{email}', '{passwd}')")
    return True, 'Succesful signup, proceed to login.', 0


def database_login(email, passwd):
    '''database login function called when users need to login to existing accounts,
    checks database for match on (email, passwd) using a simple join.'''

    cursor.execute(f"SELECT userinfo.passwd from userinfo JOIN users ON userinfo.userID = users.userID WHERE users.email = '{email}' LIMIT 1;")

    try:
        if cursor.fetchone()[0] == passwd:
            return (True, 'Succesful login', 1)
        return (False, 'Invalid login. Email or Password does not match', 1)
    
    except TypeError:
        return (False, 'Invalid email address. No user found.', 1)