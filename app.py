import os
from flask import Flask, flash, redirect, render_template, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/concert_list")
def concert_list():
    concerts = mongo.db.artists.find()
    return render_template("concerts.html", concerts=concerts)


@app.route("/delete/<artist_id>")
def delete_artist(artist_id):
    mongo.db.artists.remove({"_id": ObjectId(artist_id)})
    flash("You have deleted a Concert")
    return redirect(url_for("concert_list"))


@app.route("/add_concert")
def add_concert():
    return render_template("addconcert.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
