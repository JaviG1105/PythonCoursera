import sqlite3
import hashlib
from time import sleep
import re
from email.utils import parseaddr

conn = sqlite3.connect('/Users/JaviGarcia/Documents/Repos/GitHub/SQLite/SystemDB.db')
cur = conn.cursor()


class User:
    userName = ''
    passW = ''
    email = ''
    timesLogged = 0

    def __init__(self, userName, email, passW, timesLogged):
        self.userName = userName
        self.email = email
        self.passW = passW
        self.timesLogged = timesLogged

    def updatePass(self, newPass):
        hash = hashlib.sha256(newPass)
        self.passW = hash.hexdigest()
        try:
            conn.execute('''UPDATE User SET Password = ? WHERE Username = ?''', (self.passW, self.userName, ) )
            conn.commit()
            return 'Password updated successfully!'
        except Exception, e:
            print e

#Login
def Login(user, passW):
    hash = hashlib.sha256(passW)
    try:
        cur.execute('''SELECT * FROM User WHERE Username = ?''', (user, ))
        userData = cur.fetchone()
        userN = userData[1]
        mail = userData[2]
        passWord = userData[3]
        if userData == None: #Validating user exists
            print '''User doesn't exist'''
        if hash.hexdigest() != passWord: #Validating password is correct
            print 'Password is incorrect'
        else:
            timesL = int(userData[4])+1
            cur.execute('''UPDATE User SET TimesLogin = ? WHERE Username = ?''', (timesL, userN, ))
            conn.commit()
            #Bring user data again to get updated logged in times
            cur.execute('''SELECT * FROM User WHERE Username = ?''', (user,))
            userData = cur.fetchone()
            Inside(userData)
    except Exception, e:
        print e


def Inside(userData):
    s = User(userData[1], userData[2], userData[3], userData[4])
    print 'User {} has logged in: {} time(s)'.format(userData[1], userData[4])
    action = raw_input('What would you like to do? (Update password [U] or exit [E])\n')
    if action.upper() == 'Update' or action.upper() == 'U':
        pass1 = raw_input('Type your new password:\n')
        pass2 = raw_input('Confirm your new password:\n')
        if pass1 != pass2:
            print 'Passwords do not match'
        else:
            resp = s.updatePass(pass1)
            print resp
            Inside(userData)
    elif action.upper() == 'Exit' or action.upper() == 'E':
        print 'Thank you for using our system'
        exit()

def Register(userName, email, passW):
    hash = hashlib.sha256(passW)
    try:
        cur.execute('''INSERT INTO User (Username, email, password, TimesLogIn)
                        VALUES (?, ?, ?, 0)''', ( userName, email, hash.hexdigest() ) )
        conn.commit()
        return 'User registered successfully!'
    except Exception, e:
        print e
        return 'There has been an error'


def Main():
    answer = raw_input('''Register or Login? ('E to exit)'\n''')
    if answer.upper() == 'REGISTER' or answer.upper() == 'R':
        userN = raw_input('Type in your username:\n')
        email = raw_input('Type in your email:\n')
        passW = raw_input('Type in your password:\n')
        if not re.match(r"[^@]+@[^@]+\.[^@]+", passW):
            print 'Please enter a valid email'
        else:
            response = Register(userN, email, passW)
            print response
        Main()
    elif answer.upper() == 'LOGIN' or answer.upper() == 'L':
        userN = raw_input('Username:\n')
        passW = raw_input('Password:\n')
        response = Login(userN, passW)
    elif answer.upper() == 'EXIT' or answer.upper() == 'E':
        print 'Thank you for using our system.'
        exit()
    else:
        print 'Invalid input'
        Main()


Main()
