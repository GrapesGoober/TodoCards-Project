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


import random
import string


def generate_unique_code():
    length = 15
    characters = string.ascii_letters + string.digits
    # print(characters) = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
    unique_code = ''.join(random.choice(characters) for i in range(length))
    print(unique_code)
    return unique_code


generate_unique_code()




