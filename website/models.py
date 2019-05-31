from peewee import *
from config import DB

class Person(Model):
    firstname = CharField()
    surname = CharField()

    class Meta:
        database = DB

if __name__ == "__main__":
    DB.connect()
    DB.create_tables([Person])

    # Add some data
    Person(firstname="John", surname="Bob").save()
    Person(firstname="Jane", surname="Bob").save()
    Person(firstname="Michael", surname="Clark").save()
