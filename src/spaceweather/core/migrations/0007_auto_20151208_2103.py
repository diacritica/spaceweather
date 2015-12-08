# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151208_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sunspot',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date', models.DateTimeField()),
                ('value', models.FloatField()),
                ('units', models.CharField(blank=True, default='sunspots', max_length=50)),
                ('bogus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='sunspottype',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
                ('explanation', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('origin', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='sunspot',
            name='sunspottype',
            field=models.ForeignKey(to='core.sunspottype'),
        ),
    ]
