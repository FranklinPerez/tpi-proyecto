# Generated by Django 2.2.7 on 2019-12-03 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admon', '0015_remove_materia_estudiantes'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='estudiantes',
            field=models.ManyToManyField(blank=True, null=True, to='admon.Estudiante'),
        ),
    ]
