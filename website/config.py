import os
from peewee import MySQLDatabase

DB_NAME = 'simplerr_schema'
DB_USER = 'simplerr'
DB_PASS = 'pick-password'
DB_HOST = '127.0.0.1'
DB_PORT = 3306

DATABASE = MySQLDatabase(
    DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT
    )
