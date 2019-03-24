# NEIGHBORHOOD

A web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

## Author

Alex Ogola

## Description

This application allows its users to do the following

* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.


## Prerequisites
* Python3.6

## Installation steps
* $ git clone https://github.com/lex-of-pakawa/neighborhood
* $ cd neighborhood
* $ source virtual/bin/activate
* Install all the necessary requirements by running pip install -r requirements.txt (Python 3).

#create a database

* psql
* CREATE DATABASE neighborhood
* connect to the database \c neighborhood
* check if tables have been created \dt

#Run migrations

* python3.6 manage.py migrate
* python3.6 manage.py makemigrations hood

#Running the app

* python3.6 manage.py runserver

#testing

* python3.6 manage.py test hood


# Technologies Used

#### This project uses major technologies which are :
* HTML5
* CSS
* Bootstrap4
* Python3.6
* django
* jQuery

## Behaviour driven development
| Behaviour   |      Input     |  Output |
|----------|:-------------:|------:|
| Display posted neighborhoods | Link to the landing page |   User can view posted neighbourhoods |
| Join neighborhood | Click "Join hood" button |   User is able to view posts related to the neighborhood |
| Create neighbourhood | Click "create a hood" button  |  User is directed to a page where they can create a new neighborhood |


# License

* MIT License


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.*
