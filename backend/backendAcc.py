import emailSystem
import bcrypt
from validate_email import validate_email
import backendGameFetch as fetch

backFetch = fetch.gameFetch(fetch.API_KEY, fetch.DB_PATH)


class goldchestAccount:
    # TODO: CREATE ACCOUNT[X], ESTABLISHING DB CON, REGEX VERIFY EMAIL [x], CONNECT STEAMID [x], ?retrieveAccount
    #I THINK THE ONLY THING THAT MIGHT BE NECESSARY IS TO RETRIEVE FROM THE DB BUT THIS IS A GREAT START

    def createAccount(self, steamid, username, displayname):
        with backFetch.create_conn(fetch.DB_PATH) as con:
            sql_InsertSteamID = "INSERT INTO users (steamid, username, displayname) VALUES ('{}');".format(steamid,username,displayname)
            con.execute(sql_InsertSteamID)
            print('inserted')

        """
        #IF I NEED TO VERIFY IF THE STEAMID EXISTS
        with backFetch.create_conn(fetch.DB_PATH) as con:
            sqlSelectID = "SELECT * FROM users WHERE steamid = '{}'".format(steamid)
            for cur in con.execute(sqlSelectID):
                print("account already exists")
                #def retrieveAccount()
            else:
                sql_InsertSteamID = "INSERT INTO users (steamid, username, displayname) VALUES ('{}');".format(steamid,username,displayname)
        
        """

    def add_Email(self, email, con, username):
        #validates if the email is in the correct format.
        is_valid = validate_email(email_address=email, check_format=True, check_blacklist=True,
                                  check_dns=True, dns_timeout=10, check_smtp=True, smtp_timeout=10,
                                  smtp_helo_host='smtp.gmail.com', smtp_from_address='goldchest.steam@gmail.com',
                                  smtp_debug=False)

        #Check if the email is in DB
        with backFetch.create_conn(fetch.DB_PATH) as con:
            if is_valid: #copied from backendGameFetch.py need to verify if it works
                sqlStmt = "SELECT * FROM users WHERE email = '{}'".format(email)
                for cur in con.execute(sqlStmt): #Could we use an if statement or smthn else
                    print("error: this account already exists") #DO we want to update the email
                else:
                    sqlAddUser = "INSERT INTO users (email) VALUES ('{}');".format(email)
                    con.execute(sqlAddUser)

                    sendMail(username, message_newUser)  # message_newUser is in emailSystem.py
            else:
                print("error: not a valid email address")

    """
    dbInit - Will create and initialize tables
    """

    def dbInit(self):
        with backFetch.create_conn(fetch.DB_PATH) as con:
            con.execute('''CREATE TABLE IF NOT EXISTS 'users' (
                        'steamid' int PRIMARY KEY,
                        'username' VARCHAR(255),
                        'displayname' VARCHAR(255),
                        'email' VARCHAR(255),
                        );''')
