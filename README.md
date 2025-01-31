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
