# FirstDirectory
# TITLE
This is a Website Project. It is contructed on Django Framework.
Addtion, it is my graduation project for my python course.

# DESCRIPTION
Project name: webanhang
App name: app
Virtual Environment: venv
# Should avoid name App like me. Avoid reserved word like app, ...
The installed libraries are describled in requirements.txt
Framework: Django

# CONTENT
Manager: manage.py or django-admin command line
Database: dh.sqlite3
# You can configure database in webbanhang.setting.py. Read more refference on https://docs.djangoproject.com/en/4.2/ref/databases/ to configure other database
Project 'webbanhang
App: app
--app --
app_views package contain a lots of file.py as views.py in django
static directory contain static and media files for applying to app
tempaltes directory contain html file which will display to user
Addition, it contain some file.py like models.py, url.py, admin.py, ...
models.py: Create and manage data from database
# You can seperate to many file.py and put them at app_models package like app_views. It is easier to manage files
url.py: contain url. It will invoke app_views/'file'.py and display to user
admin.py. Register model on admin site
other 'file'.py like test.py, app.py which are created automatically by django

# RUN PROJECT
Require: Python 3.10.11 and some libraries in requirements.txt
# Use pip install -re requirements.txt to install require librabries quickly
Download: git clone https://github.com/dhpytech/FirstDirectory.git

Assuming download file are ready!
Use py manage.py runserver to run localhost on Window
# You must active virtual environment: venv/Scripts/active.bat

# STRUCTURE OF WEBBANHANG.APP
# User:
  - Registered
  - Anynomous
# Structure Page:
  # For All user:
    Home (Display all products):
    Login (Login Page)
    Register (Register Account)
    About us (Describe about page)
    Contact us (Contact to admin)
    Product: (Category of products)
    Search: (Search Product)
  # Only Register User:
    Add to cart behavior (On Home page - Add product to user cart)
    View user cart
    View and edit user profile (On Menu bar)
    Order behavior (On Cart page - make order for user then nevigate to checkout page)
    Purchase behavior (On checkout page - Comfirm order from user the wait for comfirmation from admin)

  # Author:
    Name: Võ Đăng Huân
    Email: dh.gentle.man@gmai.com
    If you have any problem or idea for my project. Let contact me by email.Thanks!

