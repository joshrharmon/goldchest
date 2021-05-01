import smtplib, ssl

port = 465 #For SSL
password = ""#input("password: ") #we can add the actual password here instead

# Create a secure SSL context
context = ssl.create_default_context()

#EMAIL
sender_email = "goldchest.steam@gmail.com" #our email needs to be changed
reciever_email = "samuel.jothimuthu@gmail.com" #sender email will need to be updated
message_test = """\
Subject: Steam Recommendations

Hello World!
This is a test message. 2

"""
message_newUser = """\
Subject: Welcome to GoldChest

Congrats on creating a new account with GoldChest!
"""

def emailMessageBuilder_USERNAME(username):
    return """\
    Subject: Welcome to GoldChest! {}

    Congrats on creating a new account with GoldChest!
    """.format(username)

def emailMessageBuilder(subject,message):
    return """\
    Subject: {}

    {}
    """.format(subject,message)


def sendMail(address, Message):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("goldchest.steam@gmail.com", password)  # We need an account that we can use
        #print("connected")
        server.sendmail("goldchest.steam@gmail.com", address, Message)



#sendMail(reciever_email, message_test)