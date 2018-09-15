from django.db import models
from ckeditor.fields import RichTextField

class Tool(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    link = models.URLField(verbose_name="Link Git de la herramienta")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "tool"
        verbose_name_plural = "tools"
        ordering = ['order', '-updated']

    def __str__(self):
        return self.name