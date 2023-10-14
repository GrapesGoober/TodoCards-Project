from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

mydb = None

@app.route("/ping")
def ping():
    response = jsonify({"message": "pong"})
    return response

@app.route("/get-cards-list", methods=["POST"])
def get_cards_list():
    
    jsonbody = request.get_json()
    deckname = jsonbody["deckname"]
    
    mycursor = mydb.cursor()
    # there is a slight typo in "cardcolor", should be "cardColor"
    # just be careful when doing queries
    mycursor.execute(
        """
        SELECT 
            cardName,
            cardDescription,
            cardDue,
            cardIsFinished,
            cardcolor
        FROM card
        WHERE deckID = (
            SELECT deckID from deck WHERE deckName = %s
        );
        """, (deckname,))
    
    result = mycursor.fetchall()
    for i, r in enumerate(result):
        result[i] = {
            "cardName": r[0],
            "cardDescription": r[1],
            "cardDue": r[2],
            "cardIsFinished": r[3],
            "cardColor": r[4]
        }

    mycursor.close()

    response = jsonify(result)
    return response


if __name__ == "__main__":
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="TodoCards"
    )
    
    # default to 127.0.0.1 port 5000
    app.run()