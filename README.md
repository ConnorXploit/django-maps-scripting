
# Proyect with Django, MapBox and more

First version of the proyect with Django


# Installation

Clone it from git

    git clone https://github.com/ConnorHack69/django-maps-scripting.git
    cd django-maps-scripting

Make sure you run pip command and manage.py using an environment based on **python==3.6.0**. For example:

    conda create -n django2env python==3.6.0
    
This creates and environment for our packages to be installed. We have to activate now that environment and start installing whatever we need. In our case, we have all at requirements.txt

## VirtualEnv Windows

    activate django2env
    
## VirtualEnv Linux

    source activate django2env
    
Now, our shell should change a bit and start by **(**django2env**)** C:\Whatever\Dir\You\Are
At this moment we are working in the virtual environment that we want to work in. Start installing all the requirements:

    pip install -r requirements.txt
    sudo apt-get install gettext

Now we can start our server:

    python manage.py runserver
    
Then in your favorite Web Browser: http://127.0.0.1:8000/

    python manage.py migrate
    python manage.py createsuperuser
    python manage.py makemigrations
    python manage.py migrate
    
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
    
So now we have inside 'locale' directory some files. We need to edit \*.**po** named one.

    #: core/templates/core/home.html:7
    msgid "This is a message"
    msgstr "Esto es un mensaje"
    
Save that file and then:

    django-admin compilemessages
    
No we have created a new language and set some translations for a message

# Editing Read The Docs document

## Installation Sphinx

    pip install sphinx sphinx-autobuild

## Initialize & Build

    mkdir docs
    cd docs/
    sphinx-quickstart

Now we have new documents into the created folder docs/. Start editing index.rst for example and than:

    make html

## More

We are working hard for uploading the next version. Wait for it
