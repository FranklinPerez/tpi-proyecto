# Generated by Django 2.2.7 on 2019-12-03 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admon', '0013_materia_estudiantes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='estudiantes',
            field=models.ManyToManyField(blank=True, null=True, to='admon.Estudiante'),
        ),
    ]
