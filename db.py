import sqlite3
from cryptography.fernet import Fernet

key = "Be1PA8snHgb1DS6oaWek62WLE9nxipFw3o3vB4uJ8ZI="  # "secret key" This must be kept secret
cipher_suite = Fernet(key)  # This class provides both encryption and decryption facilities.

#------- C O N N E C T I O N   T O   D A T A B A S E---------
def conectionDB(func):
    """This is a decorator to open and close the database"""
    def wrapper(*args, **kwargs):
        global myConection
        global myConnection2
        global myCursor
        global myAnotherCursor
        myConection = sqlite3.connect("PasswordsDB")
        myCursor = myConection.cursor()
        myConnection2 = sqlite3.connect("PasswordsDB")
        myAnotherCursor = myConnection2.cursor()

        result = func(*args, **kwargs)

        myConection.commit()
        myConection.close()

        return result
    return wrapper
#---- E N D   C O N N E C T I O N --------



#----C R E A T E S  T A B L E S --------
@conectionDB
def createDB():
    """This is a function to create the database if is not yet created"""
    try:
        myCursor.execute('''
            CREATE TABLE USERS (
            USER VARCHAR(17) UNIQUE,
            PASSWORD VARCHAR(17),
            ANSWER VARCHAR(20),
            OPTION VARCHAR(5))
            ''')

        myCursor.execute('''
            CREATE TABLE PASSWORDS_DATA (
            USER VARCHAR(17),
            NAME VARCHAR (17),
            PASSWORD VARCHAR(17),
            APP VARCHAR(20),
            URL VARCHAR(20),
            MAIL VARCHAR(20))
            ''')

    except sqlite3.OperationalError:
        pass
#------- E N D   T A B L E ---------


#------ F U N C T I O N  F O R  L O G I N -------
@conectionDB
def loginUser(user, password):
    """ Function to login
        @Return: "yes" if the password is correct, "no" if it is incorrect, "error"  if it does not exist"""
    myCursor.execute("SELECT PASSWORD FROM USERS WHERE USER='"+user+"'")
    passwordDB = myCursor.fetchall()

    try:
        passwordDB = cipher_suite.decrypt(passwordDB[0][0])
        passwordDB = passwordDB.decode("utf-8")
        if passwordDB == password:
            return "yes"
        else:
            return "no"

    except IndexError:
        return "error"
#------ E N D  F U N C T I O N -------



#------ F U N C T I O N    F O R   S A V I N G    R E C O V E R Y -------
@conectionDB
def storeRecovery(ans, option):
    #password = cipher_suite.encrypt(bytes(password, encoding='utf-8'))
    data = (ans, option)
    myCursor.execute("INSERT INTO USERS (ANSWER, OPTION) VALUES('%s', '%s')" % (data))
#------ E N D   F U N C T I O N ----------


#------ F U N C T I O N   F O R   P A S S   R E C O V E R Y -------
@conectionDB
def passRecovery(ans, opt, user):
    myCursor.execute("SELECT ANSWER FROM USERS WHERE USER='"+user+"' AND OPTION='"+opt+"'")
    answer = myCursor.fetchall()
    myAnotherCursor.execute("SELECT OPTION FROM USERS WHERE USER='"+user+"'")
    optn = myAnotherCursor.fetchall()
    
    if optn == opt and answer == ans:
        return answer
    elif optn != opt:
        return "false"
    elif answer != ans:
        return "no"
    else:
        return "error"
#------ E N D   F U N C T I O N -------------


#------ F U N C T I O N  F O R  C R E A T I N G  A C C O U N T -------
@conectionDB
def createUser(user, password):
    """Function to create new user"""
    passwd = cipher_suite.encrypt(bytes(password, encoding='utf-8'))
    #data = (user, password)
    uu = user
    pp = passwd
    myCursor.execute("INSERT INTO USERS (USER, PASSWORD) VALUES('%s', '%s')" % (uu, pp))
#------ E N D  F U N C T I O N -------




#------ F O R   M A N A G I N G   P A S S W O R D ---------
@conectionDB
def insertPasswordData(user, name, password, notes):
    """Function to save new password in the storage"""
    password = cipher_suite.encrypt(bytes(password, encoding='utf-8'))
    data = (user, name, password, notes)
    myCursor.execute("INSERT INTO PASSWORDS_DATA VALUES(?,?,?,?)", data)


@conectionDB
def readPasswords(user):
    """ Read all passwords from the user storage
        @return: A list, in each row there is a password with its corresponding name and notes"""
    myCursor.execute("SELECT NAME,PASSWORD,NOTES FROM PASSWORDS_DATA WHERE USER='"+user+"'")
    passwords = myCursor.fetchall()
    return passwords


@conectionDB
def deletePassword(user, name):
    """ Delete a password from the user storage
        @param: the user and the name associated with the password"""
    myCursor.execute("DELETE FROM PASSWORDS_DATA WHERE USER='"+user+"' AND NAME='"+name+"'")
#--------- E N D   P A S S W O R D --------

@conectionDB
def readNotes(user, name):
    """ Read a password notes
        @param: the user and the name associated with the password"""
    myCursor.execute("SELECT NOTES FROM PASSWORDS_DATA WHERE USER='"+user+"' AND NAME='"+name+"'")
    notes = myCursor.fetchall()

    return notes
