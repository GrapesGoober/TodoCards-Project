import user
import decks
import cards
import inspect

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

assert cards.check_card_view_access(mydb, 7, "dean") == True
assert cards.check_card_view_access(mydb, 7, "fay") == True
assert cards.check_card_view_access(mydb, 4, "dean") == True
assert cards.check_card_view_access(mydb, 4, "fay") == False
assert cards.check_card_view_access(mydb, 4, "ajarn") == True
assert cards.check_card_view_access(mydb, 1, "ajarn") == False

assert cards.check_subcard_view_access(mydb, 2, "bob") == False
assert cards.check_subcard_view_access(mydb, 3, "ajarn") == True
assert cards.check_subcard_view_access(mydb, 4, "dean") == True
assert cards.check_subcard_view_access(mydb, 3, "ajarn") == True
assert cards.check_subcard_view_access(mydb, 1, "ajarn") == False

assert cards.check_card_edit_access(mydb, 7, "dean") == True
assert cards.check_card_edit_access(mydb, 7, "fay") == True
assert cards.check_card_edit_access(mydb, 4, "dean") == True
assert cards.check_card_edit_access(mydb, 4, "fay") == False
assert cards.check_card_edit_access(mydb, 4, "ajarn") == False
assert cards.check_card_edit_access(mydb, 7, "ajarn") == True
assert cards.check_card_edit_access(mydb, 1, "ajarn") == False

assert cards.check_subcard_edit_access(mydb, 2, "bob") == False
assert cards.check_subcard_edit_access(mydb, 3, "dean") == True
assert cards.check_subcard_edit_access(mydb, 4, "dean") == True
assert cards.check_subcard_edit_access(mydb, 6, "ajarn") == False
assert cards.check_subcard_edit_access(mydb, 5, "ajarn") == True
assert cards.check_subcard_edit_access(mydb, 1, "ajarn") == False


decks.get_decks_list(mydb, "dean")

#cards.get_cards_list(mydb, 4, "dean")

#cards.get_subcards_list(mydb, 4, "fay")
#cards.get_subcards_list(mydb, 8, "cindy")

