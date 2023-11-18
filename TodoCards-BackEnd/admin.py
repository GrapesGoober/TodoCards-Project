
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
    if check_is_admin(mydb, admin) == True:
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


def admin_get_everything(mydb, username):
    if check_is_admin(mydb, username) == False:
        return False
    
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

