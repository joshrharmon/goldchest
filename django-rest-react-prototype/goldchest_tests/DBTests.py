from django.test import TestCase
from sqlite3 import *

class AnimalTestCase(TestCase):
    def setUp(self):
        print("This is a test for DB")
        #set up the db, connect to db
        DB_PATH='../django-rest-react-prototype/db.sqlite3'
        connection = sqlite3.connect(path, check_same_thread=False)




    def testDB(self):
        #take a user, log them in
        #compare the user email with the one inside the database
