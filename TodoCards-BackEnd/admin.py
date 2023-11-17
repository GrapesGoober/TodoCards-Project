
def check_is_admin(mydb, username):
    mycursor = mydb.cursor()
    mycursor.execute(
        """
        SELECT 
            username 
        FROM admin 
        WHERE username = %s
        """, (username,))
    is_admin = mycursor.fetchall()

    if is_admin:
        #print("is admin")
        mycursor.close()
        mydb.commit()
        return True
    return False


def delete_user(mydb, user, admin):
    if check_is_admin == True:
        mycursor = mydb.cursor()
        mycursor.execute(
            """
                DELETE FROM user
                WHERE username = %s
                """, (user,)
        )
        mycursor.close()
        mydb.commit()
        return True
    return False

# -------------------------------------------
# def get_decks_list(mydb, username):
#     mycursor = mydb.cursor()
#     mycursor.execute(
#         """
#         SELECT 
#             deck.deckid, deck.deckName, 
#             deck.deckdescription, 
#             (SELECT MIN(cardDue) FROM card WHERE card.deckid = deck.deckid AND card.cardIsFinished = '0') as nearestDue, 
#             (select GROUP_CONCAT(DISTINCT card.cardColor) as cardColors FROM card WHERE card.deckid = deck.deckid GROUP BY deck.deckid) as card_colors,
#             access.accessType
#         FROM deck, access
#         WHERE deck.deckid = access.deckid
#               AND access.username = %s
#         """, (username,))
    
#     result = mycursor.fetchall()
#     for i, r in enumerate(result):
#         if r[3] != None:
#             formatted_nearest_due = r[3].strftime("%Y-%m-%d")
#             #formatted_nearest_due = int(r[3])
#         else:
#             formatted_nearest_due = ""

#         if r[4] != None:
#             card_colors = [color.strip() for color in r[4].split(',')]
#         else:
#             card_colors = []
            
#         result[i] = {
#             "deckId": int(r[0]),
#             "deckName": r[1],
#             "deckDescription": r[2],
#             "nearestDue" : formatted_nearest_due,
#             "cardColors" : card_colors,
#             "editable" : r[5] == "edit"
#         }
#         #print(result[i]) 
#     mycursor.close()
#     mydb.commit()
#     return result
# ------------------------------------------------------

def admin_get_everything(mydb, username):
    mycursor = mydb.cursor()
    mycursor.execute(
        """
        SELECT 
            deck.deckid, deck.deckName, 
            user.username, 
            access.accessId, access.username, access.deckid, access.accessType

        FROM deck, user, access    
        """)
    
    decks_list = {}
    users = set()
    access_dict = {}
    result = mycursor.fetchall()
    for r in result:
        deck_id = int(r[0])
        deck_name = r[1]
        user_name = r[2]
        access_id = r[3]
        access_username = r[4]
        access_deckid = r[5]
        access_type = r[6]


        #organize
        decks_list[deck_id] = deck_name
        users.add(user_name)
        access_dict[access_id] = (access_username, access_deckid, access_type)

    users_list = list(users)
    output = {
        "deckslist": decks_list,
        "users": users_list,
        "access": access_dict
    }

    mycursor.close()
    mydb.commit()
    return output

