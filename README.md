ProEP_Backend
=============

Deployed URL for the back end : https://xplore-backend-staging.herokuapp.com

This is a Django project created for the ProEP project. It represents Backend
part of the project.

Commands
--------

To run the server you are required to have python 3.8.x and higher installed!!

In case you don't have it, you can install from here: \>
https://www.python.org/downloads/windows/

To run the server you need to install all the requirements and open a console window in the folder of the
project. To check whether you are in right place, you can write(ignore the '\$'
sign):

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ ls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your output contains file **manage.py**, then you are in the right folder.
Now you need to install all the requirements which can be done by running following command:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ pip install -r requirements.txt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before you proceed, you are required to have 2 environmental variables. 
Below you will find the list with variables and what do they do. 
In the same list commands will be given on how to add them via CMD(Windows). 
However, to run them, you need to start CMD as an administrator.

-   DEBUG - can **true** or **false**. Responsible for whether to run your app in debuging mode. 
    In this mode all errors are shown with more metadata. While in development should be true. In production false.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    $ setx -m DEBUG "<Your choice>"
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-   SECRET_CODE - it's a special string that you used to encrypt project's internal messaging.
    It can be found on the Heroku site. 
    Log In with corresponding credintials > Go to staging > Settings > Config Vars > Secret Key

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    $ setx -m SECRET_KEY "\<Key you found on Heroku>"

    $ setx -m RAPID_API_HOST "\<Hosts you found on Heroku>"

    $ setx -m RAPID_API_KEY "\<Key you found on Heroku>"

    $ setx -m RAPID_API_URL "\<Url you found on Heroku>"
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

And finally, after all environmentals are set and requirements installed, you can run the server.
Following command runs the server:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$ python manage.py runserver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Structure
---------

Structure of the project's folders:

-   xplore_api - main project folder, from where you define settings of the project.

-   users_api - responsible for REST of users and authentication.

-   games_api - responsible for REST of games.

-   *manage*.*py* - command file responsible for compiling and running the
    project, creating apps, and other functionality.

Super User created.
-------------------

Credentials: - Username: *admin* - Password: *Orange*

Users API
----------

Below you will find endpoints for the *Users* part of the API. All links follow same template, which is: *origin_url*/**users**/\<endpoint\>/ 

- <> - GET method - requires token - returns all users

- <> - POST method - requires username in body - creates a new user based on the information sent - possible parameters: username, password, email, groups

- **login** - POST method - returns token which you have to include in headers in all future calls(except for registering a new user). Should be included in such a way in the calls that require token: "Authorization: Token \<token\>".

- **logout** - POST method - requires token in headers - deletes the token, sent

- **me** - GET method - requires token in headers - returns a user that owns the token sent in headers, as well as profile picture, list of his friends, wishlist and favorites.

- **\<username\>** - GET method - requires token - returns a user with provided username

- **\<username\>** - PUT method - requires token - changes a user with provided username for a new user

- **\<username\>** - PATCH method - requires token - updates a user with provided username with values from body

- **\<username\>** - DELETE method - requires token - deletes a user with provided username

- **\<username\>**/change_pass/ - PATCH method -  - requires token - changes password

- **\<username\>**/profilepicture/ - POST/PATCH method -  - requires token - adds/updates a profile picture to the specified user

Wishlist/Favorites API
----------

Below you will find endpoints for the *Users* part of the API. All links follow same template, which is: *origin_url*/**users**/**\<username\>**/wishlist/ and  *origin_url*/**users**/**\<username\>**/favorites/

- <> - GET method - requires token in headers- returns the wishlist object. Works with friend's username as well. 

- <> - POST method - requires token in headers - requires **id**, **name** and **poster_url** of the game in body - creates or gets a game from the the provided id from db. After which it adds it to the list 

- <> - DELETE method - requires token in headers - requires **id*** of the game in body - removes the game from the list

Friends API
----------

Below you will find endpoints for the *Users* part of the API. All links follow same template, which is: *origin_url*/**users**/**\<username\>**/friends/

- <> - GET method - requires token in headers- returns the friends object

- <> - POST method - requires token in headers - requires **username** you want to add to list in body - Adds it to the list 

- <> - DELETE method - requires token in headers - requires **username*** of the user you want to remove in body - removes the user from the list
