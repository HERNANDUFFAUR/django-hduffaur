# Generated by Django 4.1.1 on 2022-10-04 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_persona_fecha_nacimiento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='fecha_nacimiento',
            new_name='fecha_alta',
        ),
    ]
