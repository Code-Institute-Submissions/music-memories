import os
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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
        flash('No results found')
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


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        return redirect(url_for("concert_list"))
    return render_template("register.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get
                    ("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                return redirect(url_for("login"))
        else:
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for("login"))


@app.route('/profile/<username>', methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username,
                           concerts=mongo.db.artists.find())

    if session["user"]:
        return render_template("profile.html", username=username,
                               concerts=mongo.db.artists.find())

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
