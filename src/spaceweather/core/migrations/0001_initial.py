# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Protonflux',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('value', models.FloatField()),
                ('units', models.CharField(max_length=50, default='Protons/cm2-s-sr', blank=True)),
                ('bogus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ptype',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('explanation', models.TextField(blank=True)),
                ('url', models.URLField()),
                ('origin', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='protonflux',
            name='ptype',
            field=models.ForeignKey(to='core.Ptype'),
        ),
    ]
