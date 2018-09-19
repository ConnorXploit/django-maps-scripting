from django.db import models
from ckeditor.fields import RichTextField

def custom_upload_to(instance, filename):
    old_instance = Script.objects.get(pk=instance.pk)
    old_instance.imagen.delete()
    return 'scriptimages/' + filename

class Script(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=200)
    imagen = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    @property
    def imagen_url(self):
        if self.imagen and hasattr(self.imagen, 'url'):
            return self.imagen.url
        else:
            return "/media/scriptimages/script.png"
    class Meta:
        verbose_name = "script"
        verbose_name_plural = "scripts"
        ordering = ['order', '-updated']

    def __str__(self):
        return self.name