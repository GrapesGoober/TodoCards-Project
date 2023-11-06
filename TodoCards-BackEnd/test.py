import user
import decks
import cards

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

#print(user.login(mydb, "jenny", "jennypassword"))

#print(decks.check_deck_view_access(mydb, 2, "ajarn"))
#print(decks.check_deck_edit_access(mydb, 5, "ajarn"))

#print(cards.get_cards_list(mydb, 12, "cindy"))

decks.get_decks_list(mydb, "dean")
