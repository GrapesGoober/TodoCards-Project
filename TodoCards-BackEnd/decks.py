from datetime import date
# This is the script cards.py, which will be handling all-things decks
# This includes: getting, creating, editing, finishing, and deleting decks

# Utility function to check access for your deck_id
def check_deck_view_access(mydb, deck_id, username):
    mycursor = mydb.cursor()
    mycursor.execute(
        """
        SELECT 
            deckId, username, accessType
        FROM access WHERE deckId = %s
        """, (deck_id,))
    
    result = mycursor.fetchall()
    mycursor.close()
    mydb.commit()
    for row in result:
        if (row[1] == username and (row[2] == "view" or row[2] == "edit")):
            return True
    return False

# Utility function to check access for your deck_id
def check_deck_edit_access(mydb, deck_id, username):
    mycursor = mydb.cursor()
    mycursor.execute(
        """
        SELECT 
            deckId, username, accessType
        FROM access WHERE deckId = %s
        """, (deck_id,))
    
    result = mycursor.fetchall()
    mycursor.close()
    mydb.commit()
    for row in result:
        if (row[1] == username and row[2] == "edit"):
            return True
    return False

# Retrieve all decks that the user has view or edit access to
def get_decks_list(mydb, username):

    mycursor = mydb.cursor()
    mycursor.execute(
        """
        SELECT 
            deck.deckid, deck.deckName, 
            deck.deckdescription, 
            (SELECT MIN(cardDue) FROM card WHERE card.deckid = deck.deckid AND card.cardIsFinished = '0') as nearestDue, 
            (select GROUP_CONCAT(DISTINCT card.cardColor) as cardColors FROM card WHERE card.deckid = deck.deckid GROUP BY deck.deckid) as card_colors,
            access.accessType
        FROM deck, access
        WHERE deck.deckid = access.deckid
              AND access.username = %s
        """, (username,))
    
    result = mycursor.fetchall()
    for i, r in enumerate(result):
        if r[3] != None:
            formatted_nearest_due = r[3].strftime("%Y-%m-%d")
            #formatted_nearest_due = int(r[3])
        else:
            formatted_nearest_due = ""

        if r[4] != None:
            card_colors = [color.strip() for color in r[4].split(',')]
        else:
            card_colors = []
            
        result[i] = {
            "deckId": int(r[0]),
            "deckName": r[1],
            "deckDescription": r[2],
            "nearestDue" : formatted_nearest_due,
            "cardColors" : card_colors,
            "editable" : r[5] == "edit"
        }
        #print(result[i]) 
    mycursor.close()
    mydb.commit()
    return result
    #---------------------------------------
    """
    expected_results = [
        {
            "deckId" : 1,
            "deckName" : "QuickDeck",
            "deckDescription" : "Some deck",
            "nearestDue" : "12 June 2029"
        }
    ]
    return expected_results
    """

# Edits a deck using deck_info
# must also check for edit access of that deck_id
# returns True or False
def edit_deck(mydb, deck_info, username):

    if check_deck_edit_access(mydb, int(deck_info["deckId"]), username):
        mycursor = mydb.cursor()
        mycursor.execute(
            """
            UPDATE deck
            SET deckName = %s,
                deckDescription = %s

            WHERE deckid = %s
            """,
            (deck_info["deckName"], deck_info["deckDescription"], int(deck_info["deckId"]))
        )
        mycursor.close()
        mydb.commit()
        return True
    return False


# deletes a deck using deck_id
# must also check for edit access of that deck_id
# returns True or False
def delete_deck(mydb, deck_id, username):
    if check_deck_edit_access(mydb, deck_id, username):
        mycursor = mydb.cursor()
        mycursor.execute(
            """
                DELETE FROM deck
                WHERE deckid = %s
                """, (deck_id,)
        )
        mycursor.close()
        mydb.commit()
        return True
    return False

# Generates a unique sharecode, inserts to share table, and returns it
# must also check for edit access of that deck_id to get sharecode
# returns share code, or false
def get_sharecode(mydb, deck_id, username):
    return "some_code_1234"

# Recieves a sharecode and allow access
# must check sharecode integrity (expiration and deck exists)
# then a new access record onto access table
# returns True if success, false otherwise
def recieve_sharecode(mydb, sharecode, username):
    return "Unimplemented"


def create_deck(mydb, deck_info, username):
    mycursor = mydb.cursor()
    mycursor.execute(
        """
        INSERT INTO `deck` (`deckName`, `deckDescription`) 
        VALUES (%s, %s)
        """,
        (deck_info["deckName"], deck_info["deckDescription"])
    )

    deck_id = mycursor.lastrowid
    addAccess(mydb, deck_id, "edit", username)
    return True


'''
Note that this will not generate a duplicate access record when another already exists. 
If the target access already exists, simply do nothing and return true. 
(also, this function does not need to check access for the access giver. 
Since this function will be used only by create_deck and recieve_sharecode, 
both of these functions will check the giver's access beforehand)
'''
def addAccess(mydb, deck_id, access_type, username):
    mycursor = mydb.cursor()
    mycursor.execute(
        """
        SELECT 
            username, deckid, accessType 
        FROM access
        WHERE username = %s
            AND deckid = %s
            AND accessType = %s
        """, (username, deck_id, access_type))
    
    result = mycursor.fetchall()
    mycursor.close()
    mydb.commit()

    if not result:
        mycursor = mydb.cursor()
        mycursor.execute(
            """
            INSERT INTO `access` (`username`, `deckId`, `accessType`) 
            VALUES (%s, %s, %s)
            """,
            (username, deck_id, access_type)
        )
        mycursor.close()
        mydb.commit()

    #else:
        #print("record exists")
    return True


def get_access_list(mydb, deck_id, username):
    if check_deck_edit_access(mydb, deck_id, username):
        mycursor = mydb.cursor()
        mycursor.execute(
            """
                SELECT username, accessType FROM access
                WHERE deckId = %s AND username != %s
            """, (deck_id, username)
            )

        result = {}
        for i, r in enumerate(mycursor.fetchall()):
            if r[1] not in result:
                result[r[1]] = []
            result[r[1]].append(r[0])
        
        mycursor.close()
        mydb.commit()
        return result
    return False


def remove_access(mydb, deck_id, removee_username, remover_username):
    if check_deck_edit_access(mydb, deck_id, remover_username):
        mycursor = mydb.cursor()
        mycursor.execute(
            """
                DELETE FROM access
                WHERE deckid = %s
                    AND username = %s
                """, (deck_id, removee_username)
            )
        mycursor.close()
        mydb.commit()
        return True
    else:
        print("remover_username does not have access")
    return False
