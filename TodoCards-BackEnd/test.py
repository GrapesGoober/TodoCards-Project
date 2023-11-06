import user

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

# print(user.signup(mydb, "jenny", "jennypassword"))

print(user.login(mydb, "jenny", "jennypassword"))