# Instructions 28-9-2024

Docs: https://docs.djangoproject.com/en/5.1/


- Create database from MYSQL. Eg: test
- Create virtual env: 'python -m venv ve'
- Activate virtual env: 've/Scripts/activate/
- Install dependency: 'pip install mysql-connector-python'
- Create project 'django-admin startproject info'
- Run server: 'cd info' y despues 'python manage.py runserver'
- Stop Program: CTRL + C
- Migrate: python manage.py migrate

- Setup your main.py in connection (line 39)
- Run script: 'python main.py'

# Create super user

- 'python manage.py createsuperuser'
- 'python manage.py runserver
- Search localhost:8000/admin

# Create app

- python manage.py startapp <app>

# Migrations of app
- python manage.py makemigrations
- python manage.py migrate