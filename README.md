# SushiCat

- SushiCat is my idea for a sushi restaurant and for this project I wanted to focus on making a booking system for the restaurant. That being said I also wanted to create a restaurant website that looked clean and professional using everything I've learned about front end development so far in my education. In my opinion I achieved both of these features; the booking system works how I intented and the website looks how I planned. One of my biggest worries for this project was how to handle the back end development. I learnt a great deal from coding this application as I figured out how to enable users to create an account, book, edit and delete a reservation. This is definitely a project that I would love to come back to and improve appon further after this course as I believe it is my highest quality project yet.

- Image

### Link to deployed site:

![Finished website on different devices]()

[Photo taken using amiresponsive.com](https://ui.dev/amiresponsive)

---

## Link to Project Board

https://github.com/users/MadeleineWalder/projects/5

Here you can see:
- The wireframe
- User Stories
- Design Features
- Structural Features
- Future Features
- Bugs

---

## Technologies:

- This site was created using these languages: Python, JavaScript, HTML and CSS.
- Frameworks/Libraries: Django and Bootstrap.
- Github and Gitpod are the platforms where I created this website. Github (and Gihub pages) for creating and storing my repositories and project board/issues, and Gitpod for writing the code.
- Heroku for deployment.
- Unicorn Revealer is an extension for Chrome which I used to help me see the different elements of my site clearly.
- [Google Fonts](https://fonts.google.com/) is where I imported my fonts from.
- [Fontawesome](https://fontawesome.com/) is the website where I sourced my social media icons.
- [Pexels](https://www.pexels.com/) is the website I used to source the hero image.
- I used the website [amiresponsive.com](https://ui.dev/amiresponsive) to show my finished site on different devices at the top of this page.

---

## Testing: 

### Supported Screens and Browsers:

- The site was viewed and tested on the Google Chrome browser
- Different screen sizes were tested using a simulator that is part of Google Chrome's dev tools
- As a result all screenshots of different screen sizes are also taken from this simulator
- Tested/ supported devices: Galaxy Fold, Moto G4, iPhone 4, 6, 7, 8, X, XR and 12 Pro, Pixel 5, Samsung Galaxy S8+, S20 Ultra and A51/71, iPad, iPad Air, Mini and Pro, Surface Pro 7, Surface Duo, Nest Hub and Nest Hub Max.

### Screen Testing

Upon opening the site the user should first see the home page:

Home page on desktop:

![homepage on desktop](/docs/screenshots/hpdesktop.jpg)

Home page on tablet:

![homepage on tablet](/docs/screenshots/hptablet.jpg)

Home page on mobile:

![homepage on mobile](/docs/screenshots/hpmobile.jpg)

Clicking on 'Menu' in the navigation bar OR the 'Menu' button should take them to the menu page:

Menu page on desktop:

![menu on desktop](/docs/screenshots/mdesktop.jpg)

Menu page on tablet:

![menu on tablet](/docs/screenshots/mtablet.jpg)

Menu page on mobile:

![menu on mobile](/docs/screenshots/mmobile.jpg)

Clicking on 'Sign-up' in the navigation bar should take them to the sign up page:

Sign up page on desktop:

![sign up on desktop](/docs/screenshots/signupdesktop.jpg)

Sign up page on tablet:

![sign up on tablet](/docs/screenshots/signuptablet.jpg)

Sign up page on mobile:

![sign up on mobile](/docs/screenshots/signupmobile.jpg)

Clicking on 'Sign-in' in the navigation bar should take them to the sign in page:

Sign in page on desktop:

![sign in on desktop](/docs/screenshots/signindesktop.jpg)

Sign in page on tablet:

![sign in on tablet](/docs/screenshots/signintablet.jpg)

Sign in page on mobile:

![sign in on mobile](/docs/screenshots/signinmobile.jpg)

Clicking on 'Sign-out' in the navigation bar should take them to the sign out page:

Sign out page on desktop:

![sign out on desktop](/docs/screenshots/signoutdesktop.jpg)

Sign out page on tablet:

![sign out on tablet](/docs/screenshots/signouttablet.jpg)

Sign out page on mobile:

![sign out on mobile](/docs/screenshots/signoutmobile.jpg)

Clicking on 'Bookings' in the navigation bar OR the 'Book' button should take them to the bookings page:

Booking page on desktop:

![Booking page on desktop](/docs/screenshots/bdesktop.jpg)

Booking page on tablet:

![Booking page on tablet](/docs/screenshots/btablet.jpg)

Booking page on mobile:

![Booking page on mobile](/docs/screenshots/bmobile.jpg)

However if the user is not signed in yet they will be required to sign in first:

Require sign in to book on desktop:

![Booking page on desktop](/docs/screenshots/sidesktop.jpg)

Require sign in to book on tablet:

![Booking page on tablet](/docs/screenshots/sitablet.jpg)

Require sign in to book on mobile:

![Booking page on mobile](/docs/screenshots/simobile.jpg)

Clicking on the 'Add Booking' button should take them to the add booking page:

Add booking page on desktop:

![add booking page on desktop](/docs/screenshots/adesktop.jpg)

Add booking page on tablet:

![add booking page on tablet](/docs/screenshots/atablet.jpg)

Add booking page on mobile:

![add booking page on mobile](/docs/screenshots/amobile.jpg)

When the user clicks on the date field they will see this calendar to help them pick a date:

![add booking date picker](/docs/screenshots/date.jpg)

The time field also has a similar function:

![add booking time picker](/docs/screenshots/time.jpg)

None of the form fields can be left blank:

![the name field is required](/docs/screenshots/fname.jpg)

![the date field is required](/docs/screenshots/fdate.jpg)

![the time field is required](/docs/screenshots/ftime.jpg)

![the number of people field is required](/docs/screenshots/fpeople.jpg)

If the user inputs a date in the past, they will be notified that they must enter a date in the future.

![the date error message](/docs/screenshots/datepicker2.jpg)

The same thing will happen if they try to edit a booking date to a date that is older than the current date.

Likewise if they edit or create bookings on the same date they will notified and the booking form refreshed:

![the date error message](/docs/screenshots/doublebooking.jpg)

Clicking on the 'Edit' button on a booking should take them to the edit booking page:

Edit booking page on desktop:

![Edit booking page on desktop](/docs/screenshots/edesktop.jpg)

Edit booking page on tablet:

![Edit booking page on tablet](/docs/screenshots/etablet.jpg)

Edit booking page on mobile:

![Edit booking page on mobile](/docs/screenshots/emobile.jpg)

Clicking on the 'Delete' button should trigger the delete modal on the bookings:

Delete booking page on desktop:

![Delete booking page on desktop](/docs/screenshots/ddesktop.jpg)

Delete booking page on tablet:

![Delete booking page on tablet](/docs/screenshots/dtablet.jpg)

Delete booking page on mobile:

![Delete booking page on mobile](/docs/screenshots/dmobile.jpg)

---

### Validator Testing

- I used the [W3C HTML Validator](https://validator.w3.org/#validate_by_input) to test my html.

The home page:
The results showed an error in two places where an anchor tag is wrapping the buttons. I did some research and I couldn't find out **why** this is bad practise. I even found one website which gave an example of some html where the button was wrapped in anchor tags. The website actually offers coding course which I almost enrolled on myself. A link to the page is here: https://www.shecodes.io/athena/17038-how-to-add-a-link-to-my-button-in-html

The only other solution I could find was to remove the button tags and use divs instead, but style them like buttons. Unfortunately I dont think I will have time to implement this as I'm worried about the implications this will cause so close to my deadline.

![The W3C Validator showing my HTML](/docs/screenshots/hpvalid1.jpg)

The menu page:
Here there were no errors.

![The W3C Validator showing my HTML](/docs/screenshots/bvalid.jpg)

The booking page:
I made sure to add a booking here before copying the source code so that could be tested too. I'm not sure what is going on with these errors. I have been looking over my code and all the errors say I have unclosed elements but all of mine are closed properly.
As an example the final error says that the main tag is unclosed, but you can clearly see that it is:

![The W3C Validator showing my HTML](/docs/screenshots/vbvalid.jpg)

![The W3C Validator showing my HTML](/docs/screenshots/main.jpg)

The Sign-up page:
No errors.

![The W3C Validator showing my HTML](/docs/screenshots/suvalid.jpg)

The Sign-in:

![The W3C Validator showing my HTML](/docs/screenshots/sivalid.jpg)

The Sign-out page:

![The W3C Validator showing my HTML](/docs/screenshots/sovalid.jpg)

- I used the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) to test my CSS. There were no errors:

![The W3C Validator showing my CSS](/docs/screenshots/cssvalid.jpg)

- I have tested my site using the devtools Lighthouse feature.

![The lighthouse report](/docs/screenshots/lhreport.jpg)

---

## Deployment:

### Gitpod

- Typing 'python3 manage.py runserver' into the Gitpod terminal allows you to view a preview of the site in a browser
- Every time a secton of code is added the browser can be refreshed to see the change, sometimes you need to press ctrl + shift + R for changes to be updated
- To save and commit progress, type 'git add .' into the terminal to add all your changes followed by 'git commit -m' and then your message describing what you did in double quotes
- Typing 'git push' will then push your code, and this should be done at the end of every coding session or whenever you want an already deployed site to be updated


### Github and Github Pages

- To deploy my site I first went to Github and found my project repository on the left hand side and clicked it
- I then clicked on 'Settings' and then the 'Pages' option on the left   
- Here I changed the branch from 'none' to 'main'
- Finally I clicked save and after a short while it produced a link to my deployed site


### Heroku

- For this project I deployed to Heroku at the begining of the project. Deploying early can save you a lot of time later on.
- To do this I created a new Heroku app which I also named sushicat.
- In the app settings I made sure to add all of the config vars I would need: the secret key, the port and my database url which I got from ElephantSQL.
- I made sure to comment out the old database 'db.sqlite3' in the settings.py file and added in my new database url.
- I also added my Heroku Hostname to the allowed hosts list.
- Back in Heroku I went to the deployment tab for my app and selected Github. Then I searched for and selected my repository.
- At the bottom of the page I ticked the box to enable automatic deploys, and the clicked deploy.

Link to deployed site:

---