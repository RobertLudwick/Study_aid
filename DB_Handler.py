#Handles all the DB work so it's not in main
# Check log for all inputs into the DB

#import importlib
import sqlite3 as sl
con = sl.connect('Study.db')

sql = ""

#This will run multiple commands
def CallDB(command):
    with con:
        data = con.execute(command)
        return data
        # for i in data:
        #     # this print is specific to querying the Notes table
        #     print (f"{i[0]} {i[1]} {i[2]} {i[3]}")

# Retrieves all rows in a DB
def RetrieveDB(table):
    with con:
        data = con.execute("SELECT * FROM " + table)
        return data

def RetrieveOrderedDB(table,column):
    with con:
        data = con.execute("SELECT * FROM %s ORDER BY %s" % (table, column))
        return data

def SearchDB(table, searchcol, searchrow):
    sql = "SELECT * FROM " + table + " WHERE " + searchcol + " =  '" + str(searchrow) + "'"
    with con:
        data = con.execute(sql)
        return data

def UpdateDB(table, col, row, searchcol, searchrow):
    sql = "UPDATE " + table + " SET " + col + " = " + row + " WHERE " + searchcol + " =  '" + str(searchrow) + "'"
    with con:
        data = con.execute(sql)
        return data

def InsertIntoDB(table, list):
    list = str(list)[1:-1]
    sql = "Insert INTO %s VALUES (%s)"  % (table, list)
    with con:
        data = con.execute(sql)
        return data