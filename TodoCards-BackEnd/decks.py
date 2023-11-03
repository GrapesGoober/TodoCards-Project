# This is the script cards.py, which will be handling all-things decks
# This includes: getting, creating, editing, finishing, and deleting decks

# Utility function to check access for your deck_id
def check_deck_view_access(mydb, deck_id, username):
    return True

# Utility function to check access for your deck_id
def check_deck_edit_access(mydb, deck_id, username):
    return True

# Retrieve all decks that the user has view or edit access to
def get_decks_list(mydb, username):
    expected_results = [
        {
            "deckId" : 1,
            "deckName" : "QuickDeck",
            "deckDescription" : "Some deck"
        }
    ]
    return expected_results

# Edits a deck using deck_info
# must also check for edit access of that deck_id
# returns True or False
def edit_deck(mydb, deck_info, username):
    return True

# deletes a deck using deck_id
# must also check for edit access of that deck_id
# returns True or False
def delete_deck(mydb, deck_id, username):
    return True

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
    return True