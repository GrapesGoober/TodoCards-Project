from flask import Flask, request, jsonify, session
from flask_cors import CORS
import mysql.connector

import cards, user

# connects to mysql
# sets this up as a global variable
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="TodoCards"
)

# sets up some flask stuff
app = Flask(__name__)
app.secret_key = "some really useless key lol"
CORS(app, origins=["http://localhost:5173"], supports_credentials=True)
app.config['SESSION_COOKIE_SAMESITE'] = "None"
app.config['SESSION_COOKIE_SECURE'] = True

# a debugging route that responds with "pong"
@app.route("/ping")
def ping():
    response = jsonify({"message": "pong"})
    return response

# authenticates a user and sets a session variable "userid"
@app.route("/login", methods=["POST"])
def login():
    jsonbody = request.get_json()
    username = jsonbody.get("username")
    password = jsonbody.get("password")

    # login function returns either userid or false
    status = user.login(mydb, username, password)

    if status == True:
        session["username"] = username

    return jsonify(status)

@app.route("/logout", methods=["GET"])
def logout():
    if "username" in session:
        session.pop('username', default=None)
    return ""

# retrieve a list of cards using deckname. 
# this also performs user authentication to make sure that user has access to that card
@app.route("/get-cards-list", methods=["GET"])
def get_cards_list():
    deckname = request.args["deckname"]
    username = session.get("username")
    if username == None:
        return jsonify({"Error": "User hasn't logged in"})

    result = cards.get_cards_list(mydb, deckname, username)
    response = jsonify(result)
    return response

@app.route("/edit-deck", methods=["POST"])
def edit_deck():
    return "Unimplemented"

@app.route("/edit-card", methods=["POST"])
def edit_card():
    return "Unimplemented"

@app.route("/edit-subcard", methods=["POST"])
def edit_subcard():
    return "Unimplemented"

@app.route("/get-sharecode", methods=["GET"])
def get_sharecode():
    return "Unimplemented"

@app.route("/recieve-sharecode", methods=["GET"])
def recieve_sharecode():
    return "Unimplemented"

# the entry point of the code
if __name__ == "__main__":
    # runs app, default to 127.0.0.1 port 5000
    app.run(debug=True)