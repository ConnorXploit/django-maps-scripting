# Generated by Django 2.0.2 on 2018-09-18 00:03

from django.db import migrations, models
import victimas.models


class Migration(migrations.Migration):

    dependencies = [
        ('victimas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='victima',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=victimas.models.custom_upload_to),
        ),
    ]
