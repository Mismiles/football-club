## Football club website

The project aims to make a Football club website for the team Rajputs Del Mundo. 

The website is designed for team members to have access to the member features, fans to know about the club, people to purchase products, team members to show their profiles, match reports and highlights to be viewed, so that the club could be "out there" in the world.
 
## UX
The website has a few audiences.

Firstly fans who want to keep updated about the club.

Secondly club members who have a platform to express themselves.

Thirdly, sponsors who wish to work with the club.

Forthly football fans who come accross the webpage.

As a club fan, I would like to keep updated about the football club.
As a club fan, I would like to purchase merchandise and the club kit.
As a club fan, I would like to know about news related to the club.
As a club fan, I would like to know about match fixtures and results.

As a club member, I would like to know about match fixtures and results.
As a club member, I would like to know about news related to the club.
As a club member, I would like to purchase merchandise and the club kit.
As a club member, I would like to have my own club member profile. 
As a club member, I would like to pay for matches and training sessions.

As a potential sponsor, I would like to be able to contact the club for potential collaboration.


## Wireframe

No wireframe was made for the project.

## Features

The site has the club profile and about information showing its origin. 
The site has relevant social media links for facebook, instagram and twitter.
The site has email and telephone number links to contact the organisers.
The site has a news section for club news.
It also has a matches section to show past and future matches.
The site has a team section for team members.
The site has a shop section to buy products and subscriptions.
The site has a contact form for users to contact the club.
The site has an admin app for admins to control the site.
The site has a user login system for users.

### Existing Features
- There is a shop feature which includes the club kits and fees for members.

- There is a "news" section whereby admins can post news about the club.

- A "matches" section exists to add match reports to the site.

### Features Left to Implement
- Team profiles for specific players to add their information.

- A fixtures and results app to show upcoming fixtures and past results.


## Technologies Used

The technologies used include:

- [Html]
The basis of the project was made using HTML

- [CSS]
CSS was used to add styles on top of Bootstrap

- [Bootstrap] (https://getbootstrap.com/)
Bootstrap was used for styling, the form and formatting positioning.

- [Vanilla Javascript] 
This project uses javascript to add functionally. Additionally it uses Javascript to calculate 
ideal body weight, body mass index, creatinine clearance (kidney function), the initial dose of vancomycin, 
the maintenance dose of vancomycin and the frequency of monitoring of the drug.

- [JQuery](https://jquery.com)
The project uses **JQuery** to simplify DOM manipulation. In this project, it was only used for the bootstrap features.

[Python] Python was used to process the backend functionality to the application.

[Django] Django was used to link the front and backend of the application.

## Testing
- News posts:
To test the news posting, simply login as an adminstrator. Go to "admin". Fill out a post and click "submit". Then go back to the "news" section of the site to see it.

- Match reports:
To test the match reports, simply login as an adminstrator. Go to "matches". Fill out a match report and click "submit". Then go back to the "matches" section of the site to see it.

-Shop:
To test the shop functionality: click "shop". Search for or select a product. Add the product to the bag. Update the quantity as needed. Go to secure checkout. Fill in the details and card number. Use the dummy card number "4242 4242 4242 4242", fill out any future date and 3 digits for the "CVC". Fill out a dummy zip code (note the stripe code will automatically format the customer’s billing address country based on their card number). Click complete order. The transaction is now complete.

- Contact
To test the contact form, click "contact". Fill out the form and click "submit".

## Deployment

To run the project, simply go to https://club-football.herokuapp.com/

## To run locally

Simply clone this repository using $ git clone https://github.com/Mismiles/football-club.git

To install dependencies for the app to run from the requirements.txt file, run the following command in the terminal "pip3 install -r requirements.txt"

Set your environment variables e.g. IP: 127.0.0.1 and PORT: 5000 to view the site in the browser.

If running locally, set debug to "True" at the very bottom of app.py.

Ensure you have a secret key set.

Run the code in an IDE (Integrated development environment) by loading "python3 manage.py runserver" (note the app was built using python3)

## Credits

- Huge credit to the Rajputs Del Mundo team for their input and permission to be used as part of the project.

- Many thanks to the team at Code Institute for their support, feedback and patience.

### Content
- The front end design was obtained from this template, (https://colorlib.com/wp/template/sportz/) which is also referenced in the footer. 

- The bag, products, checkout, stripe payments, profiles and admin application was taken from the course content.

-The news section was built adapting code from: https://djangocentral.com/building-a-blog-application-with-django/

-The contact form was built adapting code from: https://learndjango.com/tutorials/django-email-contact-form

### Media
Some of the shop stock images and the initial large picture blocks for the matches, team, a nrews post and contact section were obtained from https://www.pexels.com/ .

The images and videos outside of this were obtained (with permission) from the club members. 

### Acknowledgements
The team at codeinstitute for the tutorials.
Special thanks to the tutors for their patience when answering queries. 
