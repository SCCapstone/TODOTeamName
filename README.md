# TODOTeamName

We are working on a meal planning app that will allow users to quickly find and prepare recipes suited to their induvidual lifestyle. Our goal is to make healthy eating and meal planning simple and intuitive

## External Requirements

In order to build this project you first have to install:

* [Django](https://docs.djangoproject.com/en/3.2/topics/install/)
* [Python](https://www.python.org/downloads/)
* [PostgreSQL](https://www.postgresql.org/download/)

## Setup

In order to log in as an admin you will need to execute the following commands in the console :
python manage.py migrate 
python manage.py createsuperuser 

The first command will create the database tables, including where your user info will be stored.
The second command will prompt you to create a log in info. 

## Running

You need to first initialize the database by running the databaseinitialization.sql script in psql
To launch the server you need to type:
python manage.py runserver in to console.
After this visit your localhost in a webbrowser of choice. 
URLs will be added here along with what features they provide as they are created for easy access.

# Deployment
This section is pending

# Testing

Tests for this app are located in the Tests directory. Note that you must have Chrome installed on your machine in order to run tests. 

## Unit tests
This section is pending

## Behavioral tests
- Pantry Test: to run this test, cd into the Tests directory and run `python pantryTest.py`


# Authors
Garrison Davis - grd1@email.sc.edu  
Isaac Luther - iluther@email.sc.edu  
Eiman Najjar - enajjar@email.sc.edu  
Carol Juneau - cjuneau@email.sc.edu  
Matthew Lewis - mrl4@email.sc.edu
