import user

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="TodoCards"
)


# user.signup(mydb, "admin1", "admin1123")
# user.signup(mydb, "admin2", "admin2123")
# user.signup(mydb, "admin3", "admin3123")
# user.signup(mydb, "admin4", "admin4123")

assert user.login(mydb, "admin4", "admin4123") == True