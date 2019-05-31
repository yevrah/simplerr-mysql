from peewee import MySQLDatabase

DB = MySQLDatabase(
    'simplerr_schema',
    user='simplerr',
    password='pick-password',
    host='127.0.0.1',
    port=3306
)
