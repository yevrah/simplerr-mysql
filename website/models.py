from peewee import *
import config

class Person(Model):
    firstname = CharField()
    surname = CharField()

    class Meta:
        database = config.DATABASE

if __name__ == "__main__":
    config.DATABASE.connect()
    config.DATABASE.create_tables([Person])

    # Add some data
    Person(firstname="John", surname="Bob").save()
    Person(firstname="Jane", surname="Bob").save()
    Person(firstname="Michael", surname="Clark").save()
