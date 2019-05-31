import os
from peewee import MySQLDatabase
#from common.database import MystroPooledConnection

DB_SCHM = 'simplerr_schema'
DB_USER = 'simplerr'
DB_PASS = 'pick-password'
DB_HOST = '127.0.0.1'
DB_PORT = 3306

DATABASE = MySQLDatabase(
    DB_SCHM,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT
    )

# DATABASE = SimplerrPooledConnection(
#     DB_SCHEMA,
#     max_connections=150,
#     timeout=60,
#     stale_timeout=60, **{
#         'host': DB_HOST,
#         'port': DB_PORT,
#         'user': DB_USER,
#         'passwd': DB_PASSWD
#     }
# )

