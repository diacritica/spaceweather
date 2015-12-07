# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151207_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Electronflux',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('value', models.FloatField()),
                ('units', models.CharField(max_length=50, blank=True, default='Electrons/cm2-s-sr')),
                ('bogus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Etype',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('explanation', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('origin', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='protonflux',
            name='ptype',
            field=models.ForeignKey(to='core.Ptype', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electronflux',
            name='etype',
            field=models.ForeignKey(to='core.Etype'),
        ),
    ]
