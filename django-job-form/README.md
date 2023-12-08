# install Django 
pip install django

# To setup Django project
django-admin startproject mysite .  

# To create Django Job App
python3 manage.py startapp job_application

# To run Django App
python3 manage.py runserver

# To create database migration
python3 manage.py makemigrations

# To create a table
python3 manage.py migrate


# setings.py
# Email Configuration

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'XXXXXXX@gmail.com'
EMAIL_HOST_PASSWORD = 'password'