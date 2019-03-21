## Gallery

A personal gallery application that I display my photos for others to see.

## Author

Alex Ogola

# DESCRIPTION

This is an app that allows users to view photos and get information about where the photos were taken and a brief descricption of the photos.

#### Gallery Categories
* Art
* Fashion
* Luxury
* Food


## Prerequisites
* Python3.6

## Installation steps
* $ git clone https://github.com/lex-of-pakawa/gallery
* $ cd gallery
* $ source virtual/bin/activate
* Install all the necessary requirements by running pip install -r requirements.txt (Python 3).

#create a database

* psql
* CREATE DATABASE gallery
* connect to the database \c gallery
* check if tables have been created \dt

#Run migrations

* python3.6 manage.py migrate
* python3.6 manage.py makemigrations gallerys

#Running the app

* python3.6 manage.py runserver

#testing

* python3.6 manage.py test gallerys




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
| Display Images | Link to the landing page |   User can view different Images |
| Expand Image (View full size) | Click "View Full Size" button |   Expanded Image |
| View More Details | Expand Image |  More details appear on the right side of the expanded image |
| Copy a link to the photo | Click "Copy Link" button in the details section |  Link is copied to the clipboard |


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
