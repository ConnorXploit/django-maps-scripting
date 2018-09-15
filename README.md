
# Proyect with Django, MapBox and more

Welcome to PentestingLab project. We are working hard on this project with Django, MapBox and more.

# Installation

## Downloading

Clone it from git

    git clone https://github.com/ConnorHack69/django-maps-scripting.git
    cd django-maps-scripting
    
## Create VirtualEnv

Make sure you run pip command and manage.py using an environment based on **python==3.6.0**. For example:

    conda create -n django2env python==3.6.0
    
This creates and environment for our packages to be installed. We have to activate now that environment and start installing whatever we need. In our case, we have all at requirements.txt

## VirtualEnv Windows

    activate django2env
    
## VirtualEnv Linux

    source activate django2env
    
Now, our shell should change a bit and start by **(django2env)** /your/working/directory
At this moment we are working in the virtual environment that we want to work in. Start installing all the requirements:

    pip install -r requirements.txt
    sudo apt-get install gettext
    
# Running

Now we can start our server:

    python manage.py runserver
    
Then in your favorite Web Browser: http://127.0.0.1:8000/

# BBDD

For starting the BBDD we have to migrate and create super user:

    python manage.py migrate
    python manage.py createsuperuser
    
# Apps

For stating a new app, we have to type:

    ``python manage.py start nameAppHere``

Then, for implement that app, we have to add it in our **settings.py** on INSTALLED_APPS. Now, migrate this app changes:

    python manage.py makemigrations nameAppHere
    python manage.py migrate nameAppHere
    
Now, you can run the server and try your app inside the project.
    
# Translation

If you want to translate to any other language or simply help us on translating it, there are 2 commands you have to know.

First of all, create a folder named 'locale' in your root directory of your proyect and then edit settings.py for adding this on the bottom:

## settings.py

    # LOCALES
    LOCALE_PATHS = [
        os.path.join(BASE_DIR, 'locale'),
    ]

    LANGUAGES = [
        ('es', 'Español'),
        ('en', 'English'),
    ]
    
    I18N = True
    
## html files

    {% load i18n %}
    {% trans "This is a message" %}
    
Then we are going to create de translations for that. In this example im transalating to **Spanish (es)**, like this:

    django-admin makemessages -l es
    
So now we have inside 'locale' directory some files. We need to edit **po** named one.
Inside we can see some lines and we will see something like this referencing to your html template tag name created before.
The first line is the key for the translation. If we change that, the html should not work. So only write into **msgstr** the translation:

    #: core/templates/core/home.html:7
    msgid "This is a message"
    msgstr "Esto es un mensaje"
    
Save that file and then:

    django-admin compilemessages
    
No we have created a new language and set some translations for a message

For trying this, is already created, but in short words you have to create a form implementing the LANGUAGE.CODE and request.session. There are few examples to play with.

## More

We are working hard for uploading the next version. Wait for it
