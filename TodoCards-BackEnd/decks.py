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
            deck.deckid, deck.deckName, deck.deckdescription, (SELECT MIN(cardDue) FROM card WHERE card.deckid = deck.deckid) as nearestDue
        FROM deck, access
        WHERE deck.deckid = access.deckid
              AND access.username = %s
        """, (username,))
    
    result = mycursor.fetchall()
    for i, r in enumerate(result):
        formatted_nearest_due = r[3].strftime('%d %B %Y')
        result[i] = {
            "deckId": int(r[0]),
            "deckName": r[1],
            "deckDescription": r[2],
            "nearestDue" : formatted_nearest_due
        }
        #print(result[i]) for testing krub
    
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

    return "Unimplemented"

# deletes a deck using deck_id
# must also check for edit access of that deck_id
# returns True or False
def delete_deck(mydb, deck_id, username):
    return "Unimplemented"

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