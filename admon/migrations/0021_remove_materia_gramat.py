# Generated by Django 2.2.7 on 2019-12-04 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admon', '0020_grado_materias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materia',
            name='graMat',
        ),
    ]
