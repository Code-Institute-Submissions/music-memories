import os
from flask import Flask, flash, Markup, redirect, render_template, request, url_for
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


@app.route("/add_concert", methods=["GET", "POST"])
def add_concert():
    if request.method == "POST":
        concert = {
            "artist": request.form.get("artist").title(),
            "city": request.form.get("city").title(),
            "venue": request.form.get("venue").title(),
            "date": request.form.get("date"),
            "album_tour": request.form.get("album_tour").title(),
            "set_list": request.form.get("set_list").title(),
            "genres": request.form.get("genres").title(),
            "spotify_listeners": request.form.get("spotify_listeners"),
            "facebook_url": request.form.get("facebook_url"),
            "instagram_url": request.form.get("instagram_url"),
            "spotify_url": request.form.get("spotify_url"),
            "twitter_url": request.form.get("twitter_url"),
            "image": request.form.get("image"),
            "image_attribution": request.form.get("image_attribution")
        }
        mongo.db.artists.insert_one(concert)
        flash("Thank you for adding your Concert Memory")
        return redirect(url_for("concert_list"))
    return render_template("addconcert.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query")
        concerts = list(mongo.db.artists.find(
            {"$text": {"$search": query}}))

    if not concerts:
        flash(Markup(
            'No results found'
        ))
        return render_template("concerts.html")

    else:
        flash("The following results are available")
        return render_template("concerts.html", concerts=concerts)


@app.route("/edit_concert/<artist_id>", methods=["GET", "POST"])
def edit_concert(artist_id):
    if request.method == "POST":
        concert_info = {
            "artist": request.form.get("artist").title(),
            "city": request.form.get("city").title(),
            "venue": request.form.get("venue").title(),
            "date": request.form.get("date"),
            "album_tour": request.form.get("album_tour").title(),
            "set_list": request.form.get("set_list").title(),
            "genres": request.form.get("genres").title(),
            "spotify_listeners": request.form.get("spotify_listeners"),
            "facebook_url": request.form.get("facebook_url"),
            "instagram_url": request.form.get("instagram_url"),
            "spotify_url": request.form.get("spotify_url"),
            "twitter_url": request.form.get("twitter_url"),
            "image": request.form.get("image"),
            "image_attribution": request.form.get("image_attribution")
        }
        mongo.db.artists.update(
            {"_id": ObjectId(artist_id)}, concert_info)
        flash("Thanks for Updating")
        return redirect(url_for("concert_list"))

    artist = mongo.db.artists.find_one({"_id": ObjectId(artist_id)})
    return render_template("editconcert.html", artist=artist)


@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
