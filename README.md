# Cook-it!

We have developed a meal planning app that will allow users to quickly find and prepare recipes suited to their individual lifestyle. Our goal is to make healthy eating and meal planning simple and intuitive!

Visit our website here: https://secret-fortress-80929.herokuapp.com/

## External Requirements

In order to build this project you first have to install:

* [Django](https://docs.djangoproject.com/en/3.2/topics/install/)
* [Python](https://www.python.org/downloads/)
* [PostgreSQL](https://www.postgresql.org/download/)

You will also need to pip install the python requirements; you may want to use a virtual environment. Run `pip install -r requirements.txt`

## Setup

In order to log in as an admin you will need to execute the following commands in the console:
```
python manage.py migrate 
python manage.py createsuperuser 
```

The first command will create the database tables, including where your user info will be stored.
The second command will prompt you to create a log in info. 

## Running

You need to first initialize the database by running the databaseinitialization.sql script in psql.
To launch the local server you need to type `python manage.py runserver` into the console.
After this visit your localhost in a webbrowser of choice. 

# Deployment
This app was deployed using Heroku. Create a Heroku account and follow the instructions to setup and deploy the app https://devcenter.heroku.com/articles/git
After it's been deployed, run
```
heroku addons:create heroku-postgresql:hobby-dev 
```
to add the database. 
To deploy new changes that have been committed locally, run 
```
git push heroku main
```
To create a superuser for your newly deployed website, run
```
heroku run python manage.py createsuperuser
```

# Testing
Behavioral tests for this app are located in the Tests directory.  Unit tests are found in the tests.py file in their respective directory.

## Unit tests
- Unit tests are ran using the python standard library unittest module.
- To run unit tests, run python manage.py test. If you have an error regarding permissions, make sure to give admin permissions to create databases by running the following:
```
sudo su postgres
psql
ALTER USER admin CREATEDB;
```

## Behavioral tests
- Our application uses Selenium Webdriver to automate a Chrome browser for behavioral tests. Note that you must have Chrome installed on your machine in order to run tests.
- The Tests directory contains tests.py (a class with functions used by each behavioral test), and all of the behavioral tests. 
- Before running tests, ensure that you first start the local server by running `python manage.py runserver` in the console. 
- To run a behavioral test, cd into the Tests directory and run the python file for the test, e.g. `python account_test.py`. A browser window will open up and the test will be performed automatically. 

# Authors
Garrison Davis - grd1@email.sc.edu  
Isaac Luther - iluther@email.sc.edu  
Eiman Najjar - enajjar@email.sc.edu  
Carol Juneau - cjuneau@email.sc.edu  
Matthew Lewis - mrl4@email.sc.edu
