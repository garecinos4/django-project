## Djando API Project
 This project containt the folder structure and the first configuration of a Django project 

### Create new folder
Run
```
mkdir django_project
```

### Bootstrap a new Django project

Run 
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

### Run server
Run
```
python3 manage.py runserver
```

Now that the server’s running, visit http://127.0.0.1:8000/ with your web browser. 

> #### Automatic reloading of runserver
> The development server automatically reloads Python code for each request as needed. You don’t need to restart the server for code changes to take effect. However, some actions like adding files don’t trigger a restart, so you’ll have to restart the server in these cases.

> #### Projects vs. apps
> What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

Run
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

Run 

```
python manage.py runserver
```
> If you get an error page here, check that you’re going to http://localhost:8000/polls/ and not http://localhost:8000/.
