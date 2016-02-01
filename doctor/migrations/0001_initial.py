# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=50)),
                ('temp_value', models.IntegerField()),
                ('time_recorded', models.DateField()),
            ],
        ),
    ]
