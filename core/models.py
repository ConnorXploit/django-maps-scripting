from django.db import models
from ckeditor.fields import RichTextField
from victimas.models import Victima
from tools.models import Tool
from scripts.models import Script

class Home(models.Model):
    mensaje = models.CharField(max_length=200, verbose_name="Mensaje")
    victimas = Victima.objects.all()
    scripts = Script.objects.all()
    herramientas = Tool.objects.all()

    def __str__(self):
        return self.mensaje
