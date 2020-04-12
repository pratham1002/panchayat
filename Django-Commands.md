### create virtual environment:
`python -m venv myvenv`

### activate virtual environment:
`myvenv\Scripts\activate`

### install Django:
`pip install django`

### create project:
`django-admin startproject main`

### initialise git:
`git init`

### change in main directory:
`cd main`

### create app:
`python manage.py startapp panchayat`

### add comment in __init__.py so it can be pushed to github

### create urls.py in panchayat

### segregate views:
* views
* beforeLogin
* afterLogin

### create templates directory:
    base.html      // contains the base structure of all webpages

### database:
`pip install psycopg2`        (for postgres)
`python manage.py makemigrations`
`python manage.py migrate`

### start server:
`python manage.py runserver`

### handle images:
`pip install Pillow`
* add media root in setting.py and urls.py of main
* add static root

### Automatic listing of requirements:
`pip freeze > requirements.txt`