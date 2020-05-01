ProEP_Backend
=============

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
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    $ setx -m DEBUG "<Your choice>"
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-   SECRET_CODE - it's a special string that you used to encrypt project's internal messaging.
    It can be found on the Heroku site. 
    Log In with corresponding credintials > Go to staging > Settings > Config Vars > Secret Key
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    $ setx -m SECRET_KEY "<Key you found on Heroku>"
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    $ setx -m RAPID_API_HOST "<Host you found on Heroku>"
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    $ setx -m RAPID_API_KEY "<Key you found on Heroku>"
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    $ setx -m RAPID_API_URL "<Url you found on Heroku>"
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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

    games_api - responsible for REST of games.

-   *manage*.*py* - command file responsible for compiling and running the
    project, creating apps, and other functionality.

Super User created.
-------------------

Credentials: - Username: *admin* - Password: *Orange*

test
