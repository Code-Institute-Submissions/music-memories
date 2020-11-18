# Music Memories

# Introduction

The Music Memories Website is for my Data Centric Development Milestone Project Submission. It is designed to allow a user to authenticate themselves via Register or Login. Once the user has logged in they have Create, Read, Edit and Delete (CRUD) permissions to a Music Memories Database.

The Users journey is intended to be intuitive and seamless. I have created a multi-page site architecture as follows:

* Home Page with an enticing Image Carousel and Call To Action to Register or Login.
* Login & Register Pages.
* A User Profile Page.
* Community Concert Memories Page.
* Add Concert Page.
* Edit Concert Page.
* Log Out option.
# Table of Contents

*   [UX](#UX)
*   [Features](#Features)
*   [Technologies-Used](#Technologies-Used)
*   [Testing](#Testing)
*   [Deployment](#Deployment)
*   [Credits](#Credits)

# UX

This site is designed Mobile First and is responsive on all devices. Full UX documentation with User Stories is contained in the [UX Document](static/documents/UX-Documentation-Music-Memories.pdf) stored in the Documents of this GitHub Repository.

# Features

## Existing Features:

* <ins>Registration:</ins> Selecting the "Register" Button on Home Page or Navbar option brings the user to the Registration page. On this page, the user inputs their desired username (minimum of 3 characters) and password (minimum of 5 characters). If the user's registration is successful they are brought to their individual Profile page. If the user's registration is unsuccessful or the username already exists they are asked to try again via a flashed message.

* <ins>Login:</ins> Selecting the "Login" button on Home Page or via Navbar option brings the user to the Login page. On this page, the user inputs their username and password. If either is entered incorrectly, they will receive a non-specific flashed message- "Something went wrong please try again!". This ensures that third parties can't ascertain if a user already exists and try to hack the profile. Once successfully logged in the user is redirected to their individual Profile page.

* <ins>Add Concert Memory:</ins> Upon initial login the user is greeted by text on their Profile page. This page advises the user that they haven't shared any Concert Memories as of yet. The user is invited to "Add Concert Memory" via a Call To Action Button &amp; Navbar option. Once selected, the user is redirected to the Add Concert Memory page. From here, the user can input details and submit to the Database. The Concert Memory is then available on the Community Concert Memories page (Read Only) and on their Profile Page (for Read, Edit and Delete).

* <ins>Edit Concert Memory:</ins> When a user has successfully submitted a Concert Memory, it will display on the Community Concert Memories page and as an editable item on the Profile page. Selecting the "Edit" button redirects the user to the Edit Concert page. All fields are pre-populated with the existing Concert Memory and the user can edit all of it or individual elements. The user can cancel the edit by pressing the "Cancel" button.

* <ins>Delete Concert Memory:</ins> When a user has successfully submitted a Concert Memory the option to Delete the item from the Database is available. The user can complete this action by pressing the "Delete" button on their Profile page for the selected Concert Memory. 

* <ins>View &amp; Like Concert Memory:</ins> When a user is logged in they can select the Community Concert Memories page from the Navbar. Here they can view all Concert Memories in the Database. The user can select the image attribution link to view the image in its original location. The user can also visit the Artist's social platforms by selecting the associated icon. There is also an option to press the "Heart" button to add a like to another user's Concert memory.

* <ins>Search Concert Memories:</ins> On the Community Concert Memories page, a user can search for specific Artists, Cities and Genres. If there are results they will display on the same page. The user can view these and then press the "Reset" button to search again or view all posts. If there are no results available, the user will be invited to add a new Concert Memory via the Call To Action Button.

*  <ins>Logout:</ins> The user can select the Logout option on the Navbar to securely sign out of the site if using a shared device.

## Features Left To Implement:

* <ins>Embedded Social Media Links:</ins> for each user on a shared page. This will encourage further communication and interaction.

* <ins>Future Concert Planner:</ins> could also be introduced so that users can alert others to upcoming shows and arrange meet ups.

* <ins>Forum:</ins> where users can discuss Concert Memories that have been shared.

* <ins>Album Memories:</ins> could also be implemented. This is one of the reasons the site is called Music Memories, as it allows scope to further the develop the site into other Non-Concert areas.

# Technologies-Used

This website is constructed using Visual Studio Code. The programming languages utilized are HTML, CSS, Javascript/Jquery and Python. Various Python packages have also been installed via PIP including Flask and Pymongo. I utilized Bootstrap 4 as the HTML Framework and Balsamiq for Wireframes. The database utilized is a Non-Relational MongoDB database. 
# Testing

Extensive UAT(User Acceptance Testing) has been conducted and is stored in the [Testing Document](static/documents/Testing-Doc-Music-Memories.pdf) available in the Document section of this Github Repository.
# Deployment

The site is deployed and available on [Heroku](https://music-memories.herokuapp.com/).

### <ins>For a user who wishes to deploy this project locally:</ins>
Please take the following steps.
* Create your Database on [MongoDB](https://www.mongodb.com/). You can use the details contained in my project to get started.
* You will need to following installed on your Machine: PIP, git, Python3. 
* Details for installing these are freely available online.
* Install an IDE. I utilized Visual Studio Code.
* Create a new Project Folder on your Desktop.
* Open this folder in your IDE.
* Open the IDE Terminal.
* Create a Virtual Environment by typing:
    python3 -m venv .venv
* In Terminal type:
$ git clone https://github.com/david-connaughton/music-mermories
*  The project files will now display inside a folder called "music memories".
* Select all Folders & Files within "music memories" and move them to your project directory.
* In Terminal type:
    pip3 install -r requirements.txt
* Create a new file called env.py
* In this file type "import os" and then set up your environment defaults as in the grey table:

os.environ.setdefault |   Details
------ | -------
     os.environ.setdefault("IP", "0.0.0.0)
     os.environ.setdefault("PORT", "5000")
     os.environ.setdefault("SECRET_KEY" "<enter-your-secret_key>")
     os.environ.setdefault("MONGO_URI", "mongodb+srv://root:<password>@<clustername>.l6ofj.mongodb.net/<dbname>?retryWrites=true&w=majority"))
     os.environ.setdefault("MONGO_DBNAME", "<db_name>")

* Please note that you will need to enter your own "Secret Key" value, add your "Password", "Clustername" and "DB Name" where appropriate.

* Save the file.
* In Terminal type: python3 app.py
* Your project is now deployed locally.

## To Deploy to Production
* Create a new Github Repository.
* In Terminal type the following commands sequentially:
     * git init
     * git add .
     * git commit -m "Commit Message"
* In app.py remember to set "debug=False"
* To connect your project to your new Github repository type (add your username and repo name as required):
    * git remote add origin https://github.com/"user-name"/"repo-name".git
* To push your project to Github type:
    * git push -u origin main
* Create an [Heroku](https://id.heroku.com/login) account.
* Select "Create New App"
* Once your App is created, select Deployment with Github as the Deployment method.
* Select your Github Repository for connection.
* Select "Manual Deploy", this will build your site in Heroku.
* Navigate to Heroku Settings-Config Vars and press the Reveal Config Vars button.
* Input the Key Value Pairs you defined in env.py, remembering that the db-name, password, clustername and secret key variables need to be defined by you.

Key | Value
--- | ---
    IP  | 0.0.0.0
    MONGO_DBNAME | "db_name"
    MONGO_URI | "mongodb+srv://root:<password>@<clustername>.l6ofj.mongodb.net/<dbname>?retryWrites=true&w=majority"
    PORT | 5000
    SECRET_KEY | "enter-your-secret_key"

* Save these changes.
* Scroll down to domain and open your App which is now live in Production.



# Credits

### Content & Acknowledgments

* Bootstrap 4 elements are used for the Navbar & Modal elements.
* Concert Memory Images are sourced from [CC Search](https://search.creativecommons.org/).
* The User Authentication Routing is customised from a [Code Institute](https://codeinstitute.net/) Data-Centric Development Module.
* The Image Carousel CSS is sourced from [here](https://silvawebdesigns.com/how-to-change-the-bootstrap-4-carousel-to-a-fade-transition-instead-of-slide/) and was utilised to fix a rendering bug.
* The Carousel & Hero Images are supplied by [Shane Connaughton](https://www.instagram.com/connaughtonshane/?hl=en).
