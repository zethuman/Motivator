# Motivator

Description to this project [here](https://github.com/zethuman/Motivator/blob/main/Motivator%20(Django-project).pdf)

### Contents

   * [Requirements Check](#requirements-checkbox)
   * [Building](#building)
   * [Database setup](#database-setup)
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
- [ ] Django Signals - at least 4 usage
- [ ] Logging module for each app
- [x] Well structured Postman requests with all implemented methods
  - [x] separated by Folders
  - [x] using Environment variables (ex: token)
- [ ] GitHub repo with well described Readme.md



   
## Building
```
pip install virtualenvwrapper
mkvirtualenv envname
workon envname
pip install -r requirements.txt
```
## Database setup

### PostgreSQL example

1. Install PostgreSQL
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
 6. Makemigrations then migrate

## Run

```
python manage.py makemigrations
python manage.my migrate
python manage.py runserver
```
Then visit http://localhost:8000 to view the app.


## Get involved!

Master [git repository](https://github.com/zethuman/Motivator/):
 * git clone https://github.com/zethuman/Motivator.git

