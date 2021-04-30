import emailSystem
import bcrypt
from validate_email import validate_email
import backendGameFetch as fetch

backFetch = fetch.gameFetch(fetch.API_KEY, fetch.DB_PATH)


class goldchestAccount:
    # TODO: CREATE ACCOUNT, LOGIN, HELPER FN (VERIFY PASSWORD), ESTABLISHING DB CON, REGEX VERIFY EMAIL [x],
    # PASSWORD RESTRICTION [x], CONNECT STEAMID, ?FORGOT PASS

    def createAccount(self, username, password):

        vaildUsername = self.verifyEmail(username,con)

        if vaildUsername:
            validPassword = self.verifyPassword(password)
        else:
            print("error")

        if vaildUsername and validPassword:
            sqlAddUser = "INSERT INTO users (email, password) VALUES (" + username + "," + password + ");"
            con.execute(sqlAddUser)

            sendMail(username, message_newUser) #message_newUser is in emailSystem.py

        return "Success"

    def verifyEmail(self, email, con):
        #validates if the email is in the correct format.
        is_valid = validate_email(email_address=email, check_format=True, check_blacklist=True,
                                  check_dns=True, dns_timeout=10, check_smtp=True, smtp_timeout=10,
                                  smtp_helo_host='smtp.gmail.com', smtp_from_address='goldchest.steam@gmail.com',
                                  smtp_debug=False)

        if is_valid: #copied from backendGameFetch.py need to verify if it works
            sqlStmt = "SELECT * FROM users WHERE email = '{}'".format(email)
            for cur in con.execute(sqlStmt):
                return True
            else:
                return False
        else:
            return False

        #return is_valid

    def verifyPassword(self, password):
        if len(password) <= 8:
            print("error")
        else:
            #https://pypi.org/project/bcrypt/
            hashed = bcrypt.hashpw(password, bcrypt.gensalt())
            return hashed

    def verifyPasswordFrontEnd(self, password):
        #IDK if this is needed but if it is here is a stub
        #if verified on the frontend then I simply need to see if the element is in the DB
        return "Success"

    def login(self, username, password):
        return "HELLO"

    """
    dbInit - Will create and initialize tables
    """

    def dbInit(self):
        with backFetch.create_conn(fetch.DB_PATH) as con:
            con.execute('''CREATE TABLE IF NOT EXISTS 'users' (
            'gcUserID' int PRIMARY KEY,
            'email' VARCHAR(255) NOT NULL,
            'password' VARCHAR(255) NOT NULL,
            'steamUserName' VARCHAR(255),
            'steamUserID' VARCHAR(255)
            );''')


    # USER EMAIL PASSWORD STEAMID
