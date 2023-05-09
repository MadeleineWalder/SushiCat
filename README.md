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
has templates folder at the top level
uses class based views which are reusable and better than single functions like in hello django
add css folder and file into static

creating our first view
he doesnt have a media folder, is it needed at all?
*** he also has blog (restaurant equivalent) under installed apps and yet the templates file isnt in blog, its at top level so how does django find it? I guess it just works anyway

to do next:
maybe do the /hello function to check it works
add files into templates
see if the dispaly properly
if not maybe move templates folder and add inner file as shown in hello django -templates