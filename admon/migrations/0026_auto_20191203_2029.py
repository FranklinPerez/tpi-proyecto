# Generated by Django 2.2.7 on 2019-12-04 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admon', '0025_auto_20191203_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='codMat',
            field=models.IntegerField(help_text='codigo de la materia', primary_key=True, serialize=False),
        ),
    ]
