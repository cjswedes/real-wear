
## Pycharm
I chose pycharm as my IDE because I know it well. The community edition works perfectly
for python development.
* utilize google to download it
1. use `git clone https://github.com/cjswedes/real-wear.git` in a terminal to get the project
2. open pycharm, and then open that directory.

##Environment setup
Use the terminal in pycharm to run the following commands:
1. `python --version` to check the version, should be 3.5...(I am gonna try with 3.7).
I wouldnt worry too much about this. Make sure it is 3.5 or greater
2. `pip install -r requirements.txt` to install django and other dependencies
3. create a file called `.env` and put the following into it:
```
SECRET_KEY=327j6!!q5t%=hoou3gw0ffp-i46!g(aa9+$-iof50pd+xbbd(x
DB_NAME=ramsay
DB_USER=admin
DB_PASSWORD=t6AnjXPMbkP2
DB_HOST=127.0.0.1
```

##setup postgres
Check the digital ocean link in the proper readme.
~~I am not sure how to do this. I must have done it in the past since I have it already.
We want 9.5 for the version.  Google how to get it and then add documentation here if you
are the first one to do it :)~~
###Populate the DB
1. run `python manage.py flush --settings=ramsay.settings.dev` to flush your DB clear of all data
2. run `python manage.py populate_db --settings=ramsay.settings.dev` to run the population script

One thing you will for sure have to do is setup the database so that we can connect to it:
I used the pgAdminIII program on your computer to do this:
1. Open create dialog by clicking postgres 9.5 server group 
2. right click databases, and then create new...
    * Name = ramsay
    * Owner = postgres
3. create it

Now you need to create a login role so we can access it with the admin usrname and password
1. Right click Login Roles in pgAdmin click add new.
    * name = admin (or the name in your .env file)
2. change password to the DB_PASSWORD in your .env file in the definition tab
3. check all boxes in the role_priveleges tab

##Running the app
1. You need to setup a run config for ease of development:
    * find edit run configuration setting
    * select the path to `manage.py` and add `runserver --settings=ramsay.settings.dev` to the parameters
2. Run it. You should be taken to a page (localhost:8000) with something...
(not sure what will be served up depending on when you do this process)

These are just the steps that I took, there might be other ways to get here.
If there are errors, read them all to see what causes the problem,
then try to find a solution.

