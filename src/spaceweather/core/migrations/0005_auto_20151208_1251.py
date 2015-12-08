# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151207_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xrayflux',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date', models.DateTimeField()),
                ('value', models.FloatField()),
                ('units', models.CharField(default='Watt/m2', blank=True, max_length=50)),
                ('bogus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Xtype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('explanation', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('origin', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='xrayflux',
            name='etype',
            field=models.ForeignKey(to='core.Xtype'),
        ),
    ]
