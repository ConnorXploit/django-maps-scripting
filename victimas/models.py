from django.db import models
from ckeditor.fields import RichTextField

class Victima(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "victima"
        verbose_name_plural = "victimas"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
