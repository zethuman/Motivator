# Motivator

Description to this project [here](https://github.com/zethuman/Motivator/blob/main/Motivator%20(Django-project).pdf)

### Contents

1. [Building](#building)


## Building
```
pip install virtualenvwrapper
mkvirtualenv envname
workon envname
pip install -r requirements.txt
```
## Database (PostgreSQL) setup

1. Install PostgreSQL
2. Start SQL Shell
3. Enter 5 times ***Enter***
4. Create database:
   1. create database database_name;
   2. create user user_name with password 'default';
   3. grant all privileges on database database_name to user_name;
   4. \q
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

