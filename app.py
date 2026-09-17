from flask import Flask, request
import mysql.connector
from dotenv import load_dotenv
import os
app = Flask(__name__)
load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE"),
    port=int(os.getenv("MYSQL_PORT"))
)
print("MySQL connected successfully!")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    print("Name:", name)
    print("Email:", email)
    print("Message:", message)

    cursor = db.cursor()

    query = """
    INSERT INTO messages (name, email, message)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (name, email, message))
    db.commit()

    cursor.close()

    return "Message saved successfully!"

if __name__ == "__main__":
    app.run(debug=True)