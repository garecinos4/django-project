# Djando API Project
 This project containt the folder structure and the first configuration of a Django project 

## Create new folder

```
mkdir django_project
```

## Bootstrap a new Django project

 
```
django-admin startproject mysite django_project
```

The result of the command is a basic folder structure 

```
django_project/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

## Run server

```
python3 manage.py runserver
```

Now that the server’s running, visit http://127.0.0.1:8000/ with your web browser. 

> #### Automatic reloading of runserver
> The development server automatically reloads Python code for each request as needed. You don’t need to restart the server for code changes to take effect. However, some actions like adding files don’t trigger a restart, so you’ll have to restart the server in these cases.

> #### Projects vs. apps
> What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

```
python3 manage.py startapp polls
```

```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

The next step is to configure the global URLconf in the mysite project to include the URLconf defined in polls.urls. To do this, add an import for django.urls.include in mysite/urls.py and insert an include() in the urlpatterns list, so you have:

```
python manage.py runserver
```
> If you get an error page here, check that you’re going to http://localhost:8000/polls/ and not http://localhost:8000/.

## Database setup
We’ll set up the database, create your first model, and get a quick introduction to Django’s automatically-generated admin site.

> Philosophy
> Django apps are “pluggable”: You can use an app in multiple projects, and you can distribute apps, because they don’t have to be tied to a given Django installation.

To include the app in our project, we need to add a reference to its configuration class in the INSTALLED_APPS setting. The PollsConfig class is in the polls/apps.py file, so its dotted path is 'polls.apps.PollsConfig'. Edit the mysite/settings.py file and add that dotted path to the INSTALLED_APPS setting. It’ll look like this:

```
    "polls.apps.PollsConfig",
```

Now Django knows to include the polls app. Let’s run:

- Run python manage.py makemigrations to create migrations for those changes
- The sqlmigrate command takes migration names and returns their SQL
- Run python manage.py migrate to apply those changes to the database.

```
python3 manage.py makemigrations polls
python3 manage.py sqlmigrate polls 0001
python3 manage.py migrate
```

## Python interactive shell 

```
python3 manage.py shell 
```


##  Django Admin

Creating an admin user

```
python3 manage.py createsuperuser
```
