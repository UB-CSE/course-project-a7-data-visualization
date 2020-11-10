from flask import Flask, render_template, request
import pandas as pd
from src.gamedata import loldata

app = Flask(__name__)

"""
UI Code
"""


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index.html")
def returnhome():
    return render_template("index.html")

@app.route("/league1.html")
def leagueOne():
    return render_template("league1.html")

@app.route("/league1.html", methods=['POST'])
def league():
    gamertag = request.form["Gamertag"]
    region = request.form["Region"]
    try:
        df = loldata.getLolData(gamertag, region)
        return render_template("leagueStats.html", name='League Of legends Player Data', data=df.to_json())
    except Exception as e:
        return render_template("error.html")

@app.route("/cod1.html")
def codOne():
    return render_template("cod1.html")

@app.route("/codStats.html")
def codStats():
    return render_template("codStats.html")

@app.route("/error.html")
def error():
    return render_template("error.html")



if __name__ == "__main__":
    app.run(debug=True)