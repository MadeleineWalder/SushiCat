Notes:
Why do I have Cloudinary? It's not being used for anything. Uninstall?

building admin site pt1
created and migrated booking model
created superuser
run server with /admin and logged in as superuser
added test booking
seems like it already has full CRUD functionality, must be part of the django built in library
stopped server for now

building admin site pt2
dont think I need a slug field
since it already has CRUD I dont think I need a separate class for edit ans delete
if I did add these or any models to models.py, they must also be imported to admin.py so you can see them when logged in

(hello django)
models pt2
changed name of booking to display date instead of object 1 etc

(hello django)
templates
has templates folder inside my equivalent of restaurant folder not at the top level
templates folder may need to go into restaurant to work, as we have added restaurant to our installed apps in settings.py so thats where django is looking for templates ***

view creation checklist
add css folder and file into static
import Booking into views.py
I dont think I need to import generic? I dont think I need it for my site
I dont think I need all of the things he adds into his class PostList in views.py they are for a blog site
also dont think I need post_detail.html? in templates folder
note:
has templates folder at the top level
uses class based views which are reusable and better than single functions like in hello django
add base.html and index.html with basic content for now, need to add fonts/bootstrap to head

creating our first view
he doesnt have a media folder, is it needed at all?
*** he also has blog (restaurant equivalent) under installed apps and yet the templates file isnt in blog, its at top level so how does django find it? I guess it just works anyway

authorisation pt1
installed and migrated allauth
copied the templates to the templates folder to modify
4 folders, main one needed is account
commented out some code in login.html in account

authorisation pt2
not much changes to my login.html (sign up form page) as i havent written my css yet
a line in login.html in is deleted so we dont worry about forgotten passwords
i have commented it out for now, not sure how to set that up
bootstrap classes and a bunch of divs added to login.html to make the page look even better

under the video there is a link to 3 files that have been completely edited to look nice
these might be useful to have as good examples of implementing bootstrap columns/classes
theres one for login, one for logout and one for signup
you have all the same actual code in them as he does, youre just missing the styling
aka the hundreds of divs and classes