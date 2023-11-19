import user
import decks

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="TodoCards"
)

decks.get_decks_list(mydb, "ajarn")