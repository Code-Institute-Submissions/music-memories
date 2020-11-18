# Music Memories

# Introduction

The Music Memories Website is for my Data Centric Development Milestone Project Submission. It is designed to allow a user to authenticate themselves via Register of Login. Once the user has logged in they have Create, Read, Edit and Delete (CRUD) permissions to a Music Memories Database.

The Users journey is intended to be intuitive and seamless. I have created a multi-page site architecture as follows:

* Home Page with an enticing Image Carousel and Call To Action to Register or Login.
* Login & Register Pages.
* A User Profile Page.
* All-Users Concert Memories Page.
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

This site is designed Mobile First and is responsive on all devices. Full UX documentation with User Stories is contained in the [UX Document](static/documents/UX-Documentation-Music-Memories.pdf) section of this GitHub Repository.

# Features

## Existing Features:

* <ins>Registration:</ins> Selecting the "Register" Button on Home Page or Navbar option brings the user to the Registration page. On this page, the user inputs their desired username (minimum of 3 characters) and password (minimum of 5 characters). If the user's registration is successful they are brought to their individual Profile page. If the user's registration is unsuccessful or the username already exists they are asked to try again via a flashed message.

* <ins>Login:</ins> Selecting the "Login" button on Home Page or via Navbar option brings the user to the Login page. On this page, the user inputs their username and password. If either is entered incorrectly, they will receive a non-specific flashed message- "Something went wrong please try again!". This ensures that third parties can't ascertain if a user already exists and try to hack the profile. Once successfully logged in the user is redirected to their individual Profile page.

* <ins>Add Concert Memory:</ins> Upon initial login the user is greeted by text on their Profile page. This page advises the user that they haven't shared any Concert Memories as of yet. The user is invited to "Add Concert Memory" via a Call To Action Button &amp; Navbar option.Once selected, the user is redirected to the Add Concert Memory page. From here, the user can input details and submit to the Database. The Concert Memory is then available on the Community Concert Memories page (Read Only) and on their Profile Page (for Read, Edit and Delete).

* <ins>Edit Concert Memory:</ins> When a user has successfully submitted a Concert Memory, it will display on the Community Concert Memories page and as an editable item on thie Profile page. Selecting the "Edit" button redirects the user to the Edit Concert page. All fields are prepopulated with the existing Concert Memory and the user can edit all of it or individual elements. The user can cancel the edit by pressing the "Cancel" button.

* <ins>Delete Concert Memory:</ins> When a user has successfully submitted a Concert Memory the option to Delete the item from the Database is available. The user can complete this action by pressing the "Delete" button on their Profile page for the selected Concert Memory. 

* <ins>View &amp; Like Concert Memory:</ins> When a user is logged in they can select the Community Concert Memories page from the Navbar. Here they can view all Concert Memories in the Database. The user can select the image attribution link to view the image in its original location. The user can also visit the Artists social platforms by selecting the associated icaon. There is also an option to press the "Heart" button to add a like to another user's Concert memory.

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

Extensive UAT(User Acceptance Testing) has been conducted and is stored in the Testing Document available in the Document section of this Github Repository.
# Deployment

# Credits