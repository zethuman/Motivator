# Motivator

Description to this project [here](https://github.com/zethuman/Motivator/blob/main/Motivator%20(Django-project).pdf)

### Contents

   * [Requirements Check](#requirements-checkbox)
   * [Building](#building)
   * [Database setup](#database-setup)
   * [Postman Import](#postman-import)
   * [Run](#run)
   * [Get Involved](#get-involved)

   
## Requirements Checkbox   

- [x] Maximum one page description of the project, main features
- [x] Class diagram with all relations between entities
- [x] Minimum 6 models
    - [x] model inheritance
    - [x] abstract model
- [x] Minimum 4 model Manager
- [x] Minimum 6 relations between models (ForeignKey)
- [x] JWT Auth, Profile
- [x] Serializer
  - [x] at least 2 from serializer.Serializer
  - [x] at least 2 serializer from serializer.ModelSerializer
  - [x] at least 4 Serializer inheritance
  - [x] at least 6 validations
  - [x] Nested serializer
- [x] Views
  - [x] at least 2 FBV view
  - [x] at least 4 CBV APIView
  - [x] at least 6 ViewSet
  - [x] File Upload views
- [x] Django Signals - at least 4 usage
- [x] Logging module for each app
- [x] Well structured Postman requests with all implemented methods
  - [x] separated by Folders
  - [x] using Environment variables (ex: token)
- [x] GitHub repo with well described Readme.md


   
## Building
```
pip install virtualenvwrapper
mkvirtualenv envname
workon envname
pip install -r requirements.txt
```

## Database setup

#### [PostgreSQL](https://www.postgresql.org/) example

1. Install [PostgreSQL](https://www.postgresql.org/download/)
2. Start SQL Shell
3. Enter 5 times ***Enter***
4. Create database:
```
    create database database_name;
    create user user_name with password 'default';
    grant all privileges on database database_name to user_name;
    \q
```
5. Change database settings in settings.py:
 ```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database_name',
        'USER': 'user_name',
        'PASSWORD': 'default',
        'HOST': 'localhost',
        'PORT': '5432' // If you do not remember in which port your db was launched just go to step 3 and check 
    }
}
 ```
 6. [Run](#run)


## Postman Import

Link to postman collection is [here](https://www.getpostman.com/collections/9c94f14e25101d806360)

1. Run ***Postman***
2. <kbd>Ctrl</kbd> + <kbd>O</kbd> or ***File -> Import***
3. Enter tab Link
4. <kbd>Ctrl</kbd> + <kbd>V</kbd> 
5. Enter ***Continue***

## Run

```
python manage.py makemigrations
python manage.my migrate
python manage.py runserver
```
Run [Postman](#postman-import) or visit [localhost](http://localhost:8000) to view the app.


## Get involved!

Master [git repository](https://github.com/zethuman/Motivator/):
 * `git clone git://github.com/zethuman/Motivator.git`

