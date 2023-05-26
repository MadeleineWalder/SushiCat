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
- Design Features
- Structural Features
- Future Features
- Testing ?????????????????
- Bugs

---


### *Design Features:*

- **Hero Image** ...

- **Fonts** ...

- **Colour-scheme** ...



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

### Test Cases

Home page on desktop:
Home page on tablet:
Home page on mobile:

Signup page on desktop:
Signup page on tablet:
Signup page on mobile:

Signup form on desktop:
Signup form on tablet:
Signup form on mobile:

Signout page on desktop:
Signout page on tablet:
Signout page on mobile:

Login page on desktop:
Login page on tablet:
Login page on mobile:

Login form on desktop:
Login form on tablet:
Login form on mobile:

Add booking page on desktop:
Add booking page on tablet:
Add booking page on mobile:

Edit booking page on desktop:
Edit booking page on tablet:
Edit booking page on mobile:

---

### Validator Testing

- I used the [W3C HTML Validator](https://validator.w3.org/#validate_by_input) to test my html. The results showed several errors which I then fixed, resulting in 0 errors.

HTML validation after errors fixed:

![The W3C Validator showing no errors in my HTML]()

- I used the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) to test my CSS. There were a couple of minor errors which were easy to fix, resulting in 0 errors.

CSS validation after errors fixed:

![The W3C Validator showing no errors in my CSS]()

- I have tested my site using the devtools Lighthouse feature.

![The lighthouse report showing every field is green]()

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