# real-wear
visualize yourself with old museum clothes...or whatever we actualy do...
## Software Development

Ensure you have the following packages installed:

* Django      2.1.7
* Python     >3.5.2
* PostgreSQL  9.5.14

and the following pip installations:

* psycopg2-binary=2.7.7
* python-decouple=3.1

Note that the equal signs denote the versions of the pip packages.

### Setup

Use these resources to help setup:

https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html

Make sure you set up the appropriate .env file or ask for the appropriate .env file. 

### Sofwtare Workflow

Workflow is split into different setting files. Setting files are split into development (dev), testing (test), staging (stage), and production (prod). Specify appropriate settings files when running tests. Each setting file imports from the overall base setting file.

To run the server, use
`manage.py runserver --settings=ramsay.settings.dev

Make migrations with 
`manage.py makemigrations --settings=ramsay.settings.prod

Migrate with
`manage.py migrate --settings=ramsay.settings.prod


#### Project Description

#### Git practices and flow
Clone the repo into your working directory: `git clone <repo-url>`

1. Pick an Issue to work on.
2. Create a new local branch from master to do your work on
    * List branches: `git branch -a`
    * Checkout branch: `git checkout <branch_name>`, should probably always checkout master
3. Rename your local branch: `git branch -m <new-name>`
    * this is important so you dont try to merge to master once you're finished working
3. Make your changes and do your testing
4. Occasionally pull down master to merge onto your branch to stay up to date with the project.
    * Merge master onto current local branch: `git pull origin master`
    * youll have to enter a commit msg for the merge, and solve merge conflicts if they are there
    * make sure you do this before you do a Pull Request!
5. Add all your files to the staged area
    * `git add .` or `git add -A`
6. Make a commit of your files
    * `git commit -a -m "Commit msg here"`
    * Do this whenever you make progress on your issue or are done coding for awhile
7. Push your local branch to a new remote branch (not master)
    * `git push -u origin <remote-branch-name>`
    * its good practice to use the same name for the remote branch as your local branch
8. Fill out the Pull Request form: just link to the issue #
8. Get it reviewed: (just have one other person look at it)
9. Get it merged into master

