#!/usr/bin/env python

'''
mysql_access.py - Example of using raw SQL to access a mysql DB

See ~/mysql_notes/mysql_notes - for more examples of queries.

Author: Eric Saunders
May 2011
'''


import MySQLdb

# Create a connection - can also specify a host if necessary
db_connection = MySQLdb.connect(user="root", passwd="tootyrooty", db="telescope_calendar")

query = "show tables;"
cursor  = db_connection.cursor()
cursor.execute(query)

# Get everything in a big tuple
# results = cursor.fetchall()

for row in cursor:
    print row


db_connection.close()
