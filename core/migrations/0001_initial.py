# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.PositiveIntegerField(choices=[(b'lun', 1), (b'mar', 2), (b'mie', 3), (b'jue', 4), (b'vie', 5), (b'sab', 6), (b'dom', 7)])),
                ('inicio', models.TimeField()),
                ('fin', models.TimeField()),
                ('aula', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=10)),
                ('unidades_credito', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MateriaHorario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horario', models.ForeignKey(to='core.Horario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MateriaSeccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seccion', models.PositiveIntegerField()),
                ('materia', models.ForeignKey(to='core.Materia')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='materiahorario',
            name='seccion_materia',
            field=models.ForeignKey(to='core.MateriaSeccion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bloque',
            name='seccion_materia',
            field=models.ForeignKey(to='core.MateriaSeccion'),
            preserve_default=True,
        ),
    ]
