# This is the script cards.py, which will be handling all-things cards
# This includes: selecting (get), creating, updating, and deleting cards.

# Retrieve all cards within a deck
# This also has to check that the username has access to this deck
# Otherwise, returns nothing (empty list)
def get_cards_list(mydb, deckname, username):

    mycursor = mydb.cursor()
    mycursor.execute(
        """
        SELECT 
            cardId, cardName, cardDescription, cardDue, cardIsFinished, cardcolor
        FROM card WHERE deckID = (
            SELECT deckID from deck WHERE deckName = %s
        );
        """, (deckname,))
    
    result = mycursor.fetchall()
    for i, r in enumerate(result):
        result[i] = {
            "cardId": int(r[0]),
            "cardName": r[1],
            "cardDescription": r[2],
            "cardDue": r[3],
            "cardIsFinished": r[4],
            "cardColor": r[5]
        }

    mycursor.close()
    mydb.commit()
    return result
