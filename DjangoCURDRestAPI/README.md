## Pre-Requisites

# Create a virtual environemnt

python3 -m venv venv

# To activate

source venv/bin/activate

# Upgrade the pip

pip install --upgrade pip

# Install Django

pip install django

# Install Django Rest Framework

pip install djangorestframework

# Python using for PostgreSQL Database

pip install psycopg2 or pip install psycopg2-binary

## commands to create project and app

django-admin startproject <projectname>
python3 manage.py startapp <REST API>

## DB connections

DATABASE = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'restfulapiDB',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost'
    }
}

## Model creation steps
python3  manage.py makemigrations <App Name>
pythons manage.py migrate

# Run App API
python3 manage.py run server
