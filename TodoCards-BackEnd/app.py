# This is the script app.py, which is the entry point for the flask app
# This file contains the logic for routes, sessions, handling requests
# This file does not contain the logic for handling database queries & business logic
# Author: Panisara S 6422781326, Nachat K 6422770774

from flask import Flask, request, jsonify, session
import mysql.connector
import cards, user, decks

# connects to mysql
# sets this up as a global variable
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="TodoCards"
)

# sets up some flask stuff (oh, and CORS too)
app = Flask(__name__)
app.secret_key = "some really useless key lol"

# a preliminary check for login status, only excluded for non-priviledged requests
@app.before_request
def check_login():
    # only apply to previledged requests
    if request.endpoint not in ['login', 'logout', 'ping', 'signup']:
        # simply check for username status (if it's set)
        if "username" not in session:
            return jsonify(False)

# a debugging route that responds with "pong"
@app.route("/api/ping")
def ping():
    response = jsonify({"message": "pong"})
    return response

# authenticates a user and sets a session variable "userid"
@app.route("/api/login", methods=["POST"])
def login():
    jsonbody = request.get_json()
    username = jsonbody.get("username")
    password = jsonbody.get("password")

    # login function returns either true or false
    status = user.login(mydb, username, password)
    print(status)
    if status: 
        session["username"] = username
    elif "username" in session:
        session.pop("username")

    return jsonify(status)

# removes login info from session cookie
@app.route("/api/logout", methods=["POST"])
def logout():
    if "username" in session:
        session.pop('username', default=None)
    return ""

@app.route("/api/signup", methods=["POST"])
def signup():
    jsonbody = request.get_json()
    username = jsonbody.get("username")
    password = jsonbody.get("password")

    status = user.signup(mydb, username, password)
    if status: 
        session["username"] = username
    elif "username" in session:
        session.pop("username")

    return jsonify(status)

# retrieve a list of decks
@app.route("/api/get-decks-list", methods=["GET"])
def get_decks_list():
    username = session.get("username")
    result = decks.get_decks_list(mydb, username)
    return jsonify(result)


# retrieve a list of cards using deckId. 
@app.route("/api/get-cards-list", methods=["GET"])
def get_cards_list():
    deck_id = request.args.get("deckId")
    username = session.get("username")
    result = cards.get_cards_list(mydb, deck_id, username)
    return jsonify(result)

# retrieve a list of subcards using cardId. 
@app.route("/api/get-subcards-list", methods=["GET"])
def get_subcards_list():
    card_id = request.args.get("cardId")
    username = session.get("username")
    result = cards.get_subcards_list(mydb, card_id, username)
    return jsonify(result)

@app.route("/api/finish-card", methods=["POST"])
def finish_card():
    jsonbody = request.get_json()
    card_id = jsonbody.get("cardId")
    username = session.get("username")
    result = cards.finish_card(mydb, card_id, username)
    return jsonify(result)

@app.route("/api/finish-subcard", methods=["POST"])
def finish_subcard():
    jsonbody = request.get_json()
    subcard_id = jsonbody.get("subcardId")
    username = session.get("username")
    result = cards.finish_subcard(mydb, subcard_id, username)
    return jsonify(result)

@app.route("/api/edit-deck", methods=["POST"])
def edit_deck():
    jsonbody = request.get_json()
    deck_info = jsonbody.get("deckInfo")
    username = session.get("username")
    status = decks.edit_deck(mydb, deck_info, username)
    return jsonify(status)

@app.route("/api/edit-card", methods=["POST"])
def edit_card():
    jsonbody = request.get_json()
    card_info = jsonbody.get("cardInfo")
    username = session.get("username")
    status = cards.edit_card(mydb, card_info, username)
    return jsonify(status)

@app.route("/api/edit-subcard", methods=["POST"])
def edit_subcard():
    jsonbody = request.get_json()
    subcard_info = jsonbody.get("subcardInfo")
    username = session.get("username")
    status = cards.edit_subcard(mydb, subcard_info, username)
    return jsonify(status)

@app.route("/api/create-deck", methods=["POST"])
def create_deck():
    jsonbody = request.get_json()
    deck_info = jsonbody.get("deckInfo")
    username = session.get("username")
    status = decks.create_deck(mydb, deck_info, username)
    return jsonify(status)

@app.route("/api/create-card", methods=["POST"])
def create_card():
    jsonbody = request.get_json()
    card_info = jsonbody.get("cardInfo")
    username = session.get("username")
    status = cards.create_card(mydb, card_info, username)
    return jsonify(status)

@app.route("/api/create-subcard", methods=["POST"])
def create_subcard():
    jsonbody = request.get_json()
    subcard_info = jsonbody.get("subcardInfo")
    username = session.get("username")
    status = cards.create_subcard(mydb, subcard_info, username)
    return jsonify(status)

@app.route("/api/delete-deck", methods=["POST"])
def delete_deck():
    jsonbody = request.get_json()
    deck_id = jsonbody.get("deckId")
    username = session.get("username")
    status = decks.delete_deck(mydb, deck_id, username)
    return jsonify(status)

@app.route("/api/delete-card", methods=["POST"])
def delete_card():
    jsonbody = request.get_json()
    card_id = jsonbody.get("cardId")
    username = session.get("username")
    status = cards.delete_card(mydb, card_id, username)
    return jsonify(status)

@app.route("/api/delete-subcard", methods=["POST"])
def delete_subcard():
    jsonbody = request.get_json()
    subcard_id = jsonbody.get("subcardId")
    username = session.get("username")
    status = cards.delete_card(mydb, subcard_id, username)
    return jsonify(status)

@app.route("/api/get-sharecode", methods=["GET"])
def get_sharecode():
    deck_id = request.args.get("deckId")
    username = session.get("username")
    result = decks.get_sharecode(mydb, deck_id, username)
    return jsonify(result)

# Handles sharing
@app.route("/api/recieve-sharecode", methods=["GET"])
def recieve_sharecode():
    sharecode = request.args.get("sharecode")
    username = session.get("username")
    result = decks.recieve_sharecode(mydb, sharecode, username)
    return jsonify(result)

# the entry point of the code
if __name__ == "__main__":
    # runs app, default to 127.0.0.1 port 5000
    app.run(debug=True)