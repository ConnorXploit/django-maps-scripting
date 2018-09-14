
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

## More

We are working hard for uploading the next version. Wait for it
