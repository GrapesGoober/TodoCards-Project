# This is the script cards.py, which will be handling all-things decks
# This includes: getting, creating, editing, finishing, and deleting decks

# Utility function to check access for your deck_id
def check_deck_view_access(mydb, deck_id, username):
    return True

# Utility function to check access for your deck_id
def check_deck_edit_access(mydb, deck_id, username):
    return True

# Retrieve all decks that the user has access to
def get_decks_list(mydb, username):
    expected_results = [
        {
            "deckId" : 1,
            "deckName" : "QuickDeck",
            "deckDescription" : "Some deck"
        }
    ]
    return expected_results
