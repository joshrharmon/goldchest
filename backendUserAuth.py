import os
import hashlib

"""
:: passHash - Hashes user passwords
Param pw: Password to put into hash form with true-random salt
Returns hashed password with true-random salt
"""
def passHash(pw):
	salt = os.urandom(64)
	hashed = hashlib.pbkdf2_hmac('sha256', pw.encode('utf-8'), salt, 1000000)
	return (salt + hashed)
	
"""
:: passVerify - Verifies user passwords
Param hashSalt: Hashed password from user in DB
Param userInput: User password input from site
Returns true if user input password and hashed password in DB match. Else false.
"""	
def passVerify(hashSalt, userInput):
	saltDB = hashSalt[:64]
	pwhash = hashSalt[64:]
	passInput = hashlib.pbkdf2_hmac('sha256', userInput.encode('utf-8'), saltDB, 1000000)
	return true if (passInput == hashSalt) else false

"""
:: sanitizeSQL - Sanitizes SQL commands for security
Param cur: Cursor for SQL command
Param command: SQL command string with placeholders
Param *args: Varargs for allowing any amount of arguments in the SQL command
"""
def sanitizeSQL(cur, command, *args):
	cur.execute(command, [args]);
