# Generated by Django 2.2.7 on 2019-12-04 18:46

import admon.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('numReg', models.IntegerField(help_text='numero de registro', primary_key=True, serialize=False)),
                ('nota', models.DecimalField(decimal_places=2, help_text='nota del estudiante', max_digits=4)),
                ('year', models.IntegerField(default=2019)),
                ('periodo', models.CharField(blank=True, choices=[('1', '1er periodo'), ('2', '2do periodo'), ('3', '3er periodo'), ('4', '4to periodo')], default='1', help_text='Tipo de nota del estudiante', max_length=15)),
                ('tipo_nota', models.CharField(blank=True, choices=[('n', 'normal'), ('r', 'reposicion')], default='n', help_text='Tipo de notadel estudiante', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Mes',
            fields=[
                ('numMes', models.IntegerField(primary_key=True, serialize=False)),
                ('nomMes', models.CharField(max_length=15)),
                ('anio', models.CharField(help_text='año del Mes', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('codSec', models.CharField(help_text='codigo del profesor', max_length=15, primary_key=True, serialize=False)),
                ('nomSec', models.CharField(help_text='nombre del profesor', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='graEst',
        ),
        migrations.RemoveField(
            model_name='grado',
            name='seccion',
        ),
        migrations.RemoveField(
            model_name='materia',
            name='graMat',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='ciudad',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='estudiante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='admon.Estudiante'),
        ),
        migrations.AddField(
            model_name='grado',
            name='anio',
            field=models.CharField(help_text=' ', max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='grado',
            name='materias',
            field=models.ManyToManyField(blank=True, to='admon.Materia'),
        ),
        migrations.AddField(
            model_name='grado',
            name='orientador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admon.Profesor'),
        ),
        migrations.AddField(
            model_name='materia',
            name='estudiantes',
            field=models.ManyToManyField(blank=True, to='admon.Estudiante'),
        ),
        migrations.AddField(
            model_name='materia',
            name='profesor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admon.Profesor'),
        ),
        migrations.AddField(
            model_name='profesor',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admon.Usuario'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='apeEst',
            field=models.CharField(help_text='Primer y/o segundo apellido del estudiante', max_length=30),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nomEst',
            field=models.CharField(help_text='Primer y/o segundo nombre del estudiante', max_length=30),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='totalE',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='grado',
            name='nomGra',
            field=models.CharField(help_text='nombre del grado', max_length=15, primary_key=True, serialize=False, validators=[admon.validators.solo_Letras]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.CharField(blank=True, choices=[('p', 'Profesor'), ('s', 'Secretaria'), ('e', 'Estudiante'), ('a', 'Administrador'), ('o', 'Orientador')], default='e', help_text='Tipo de usuario en el sistema', max_length=10),
        ),
        migrations.DeleteModel(
            name='Registro',
        ),
        migrations.AddField(
            model_name='secretaria',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admon.Usuario'),
        ),
        migrations.AddField(
            model_name='matricula',
            name='estudiante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admon.Estudiante'),
        ),
        migrations.AddField(
            model_name='matricula',
            name='grado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admon.Grado'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='mes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admon.Mes'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='notEst',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admon.Estudiante'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='notMat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admon.Materia'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='notPro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admon.Profesor'),
        ),
    ]