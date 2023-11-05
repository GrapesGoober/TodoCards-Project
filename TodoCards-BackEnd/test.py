import user
import decks
import mysql.connector

# result = user.hash_password("password1234")
# print(result)
# print(user.is_password_correct(result, "password1234"))

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="TodoCards"
)

# This adds a new user
print(user.signin(mydb, "jenny", "jennypassword"))
# Can now login
print(user.login(mydb, "jenny", "jennypassword"))
