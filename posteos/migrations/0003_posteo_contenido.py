# Generated by Django 5.0.4 on 2024-05-13 21:16

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posteos', '0002_remove_posteo_contenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='posteo',
            name='contenido',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
