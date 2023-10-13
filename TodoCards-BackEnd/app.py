from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route("/ping")
def ping():
    response = jsonify({"message": "pong"})
    # Specify the frontend origin
    # Assuming frontend is running at localhost, port 5173
    # Check port number if you're getting CORS error!
    response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5173')
    return response

@app.route("/select-star")
def select_star():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="test"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM signup")
    myresult = mycursor.fetchall()

    response = jsonify(myresult)
    return response


if __name__ == "__main__":
    # default to 127.0.0.1 port 5000
    app.run()