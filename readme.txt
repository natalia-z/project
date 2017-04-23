//puddles

//Set up

Install Python 2.7.12 https://www.python.org/download/releases/2.7/
Install pip on Windows: http://matthewhorne.me/how-to-install-python-and-pip-on-windows-10/
Add Python and pip to Path
Install virtualenv: pip install virtualenv
Create virtualenv Puddles
Activate virtualenv: .\Scripts\activate
Install Django: pip install Django==1.10
//Project

Start project: django-admin startproject puddles
Migrate database: python manage.py migrate
Create superuser: python manage.py createsuperuser
Run locally: python manage.py runserver
Go to: http://127.0.0.1:8000/
Go to http://127.0.0.1:8000/admin
Change root location name to 'src'
Create new app 6. Create app 'appname' : python manage.py startapp appname

//Install app

2.Install 'newapp' : puddles/settings 'ISTALLED_APPS'

4.Make profile editable in admin:

Go to newapp/admin.py
Code: from .models import newapp
class newappAdmin(admin.ModelAdmin): class Meta: model = newapp

admin.site.register(newapp, newappAdmin)

//Set up static files

In static folder create new folders: static, static-only and media
Add in settings.py: if DEBUG: MEDIA_URL = '/media/' STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static-only") MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media") STATICFILES_DIRS = ( os.path.join(os.path.dirname(BASE_DIR), "static", "static") )
Set up static url: urls.py Code: from django.conf import settings from django.conf.urls.static import static ... if DEBUG: MEDIA_URL = '/media/' STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static-only") MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media") STATICFILES_DIRS = ( os.path.join(os.path.dirname(BASE_DIR,), "static", "static"), )
Collect static: python manage.py collectstatic
//Gitignore https://github.com/github/gitignore

// http://programeveryday.com/post/writing-django-views-function-based-views-class-based-views-and-class-based-generic-views/
//http://stackoverflow.com/questions/5429276/how-to-change-the-django-admin-filter-to-use-a-dropdown-instead-of-list