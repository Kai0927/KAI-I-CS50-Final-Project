import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

import Sentence_Similarity

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///Atmosphere_glossary.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/CloudSeeding")
def CloudSeeding():
    return render_template("CloudSeeding.html")

    
@app.route("/TerrainPrecipitation")
def TerrainPrecipitation():
    return render_template("TerrainPrecipitation.html")


@app.route("/AI_Application")
def AI_Application():
    return render_template("AI_Application.html")


@app.route("/Glossary_Query", methods=["GET", "POST"])
def Glossary_Query():
    """Get stock quote."""
    if (request.method == "GET"):
        return render_template("Glossary_Query.html")
    elif (request.method == "POST"):
        question = request.form.get("question")

        if (question == ""):
            return apology("Please Give Question")
        print(question)

        ### Answer from SQL ###
        #print("SELECT answer, question FROM Q_A WHERE question LIKE "+ "'%"+input_q+"%';")
        answer_db_sql = db.execute("SELECT answer, question FROM Q_A WHERE question LIKE"+ "'%"+question+"%';")

        if (answer_db_sql != []):
            answer_database = answer_db_sql
            print(answer_database)
        else:
            answer_database = [{"answer": "Data Is Not In SQLITE."}]
        
        answer_ai = Sentence_Similarity.Answer_AI(question)
    
        print(answer_ai)

        return render_template("Glossary_Query_answer.html", answer_database=answer_database, answer_ai=answer_ai, question=question)