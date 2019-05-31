# Summary

Connection strategies for MySQL - robust, simple - but no pooling.

# Baby Steps

To run this project you must first create the following user on your system

    $ mysql -u root -p

    -- Create user with password
    CREATE USER 'simplerr'@'127.0.0.1' IDENTIFIED BY 'pick-password';

    -- Give them some rights - because were going to be testing the stopping
    -- of connections we're going with admin level rights here
    GRANT ALL ON *.* TO 'simplerr'@'127.0.0.1' WITH GRANT OPTION;

    -- Reload grants table without restarting mysql
    FLUSH PRIVILEGES;

    -- Create the schema
    CREATE DATABASE simplerr_schema;

# Packages

    pip install mysqlclient simplerr


# Now lets create a config file

Create a config file to host our database settings. We'll store the connection
information in module vairables for use in testing pooled connections later.

    # file: config.py
    from peewee import MySQLDatabase

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

# Review

!()[docs/person.png]

# Let'ak whats broken...

    mysql> show processlist;
    +----+-----------------+-----------------+-----------------+---------+--------+------------------------+------------------+
    | Id | User            | Host            | db              | Command | Time   | State                  | Info             |
    +----+-----------------+-----------------+-----------------+---------+--------+------------------------+------------------+
    |  4 | event_scheduler | localhost       | NULL            | Daemon  | 808383 | Waiting on empty queue | NULL             |
    | 26 | simplerr        | localhost:56061 | simplerr_schema | Query   |      0 | starting               | show processlist |
    | 30 | simplerr        | localhost:61455 | simplerr_schema | Sleep   |      9 |                        | NULL             |
    +----+-----------------+-----------------+-----------------+---------+--------+------------------------+------------------+
    3 rows in set (0.00 sec)

    mysql> kill 30;
    Query OK, 0 rows affected (0.00 sec)

!()[docs/broken.png]

# lets fix this
