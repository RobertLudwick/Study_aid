import DB_Handler

# This is the code I made to initialize the Database

DB_Handler.CallDB(
    "CREATE TABLE users (username varchar(255), password varchar(255));"
)

DB_Handler.CallDB(
    "CREATE TABLE cards ( id int, subject varchar(255), definition varchar(255), quiz varchar(255), user varchar(255));"
)

#DB_Handler.CallDB(
#    "CREATE TABLE results ( column1 datatype, column2 datatype, column3 datatype);"
#)