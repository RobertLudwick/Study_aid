#Write your own Queries in Query.txt and execute them by running this file
# For testing purposes only
import DB_Handler
import sqlite3 as sl

con = sl.connect('Study.db')

q = open("Query.txt", "r")
sql = q.read()
q.close()
sql = sql.split("\n")

#This will run multiple commands
def CallDB(command):
    with con:
        data = con.execute(command)
        for i in data:
            print(i)
        #     # this print is specific to querying the Notes table
        #     print (f"{i[0]} {i[1]} {i[2]} {i[3]}")

for i in sql:
    print(i)
    CallDB(i)