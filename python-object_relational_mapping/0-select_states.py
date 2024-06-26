#!/usr/bin/ python3
"""sql alchemy"""
import MySQLdb
import sys

# the first step is connect to a MySQL database using the function,
# is 'module_name.connect'
# db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
# but i need to take the host, the user, the passwd and the the bd by arguments
# the next step is create a cursor the cursor object is an abstraction
# all is here "https://www.mikusa.com/python-mysql-docs/query.html"


def listAllStates(mysql_username, mysql_password, database_name):

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    # Close all cursors
    cur.close()
    # Close all databases
    db.close()

if __name__ == "__main__":
    "sqlAlchemy"

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    listAllStates(mysql_username, mysql_password, database_name)
