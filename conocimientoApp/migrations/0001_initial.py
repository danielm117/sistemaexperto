# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_nacimiento', models.DateField()),
                ('nombres', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('peso', models.DecimalField(max_digits=5, decimal_places=2)),
                ('estatura', models.IntegerField()),
                ('ejercicio', models.IntegerField()),
                ('genero', models.CharField(max_length=1)),
                ('contrasena', models.CharField(max_length=30)),
            ],
        ),
    ]
