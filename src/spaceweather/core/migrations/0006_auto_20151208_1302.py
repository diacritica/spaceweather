# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151208_1251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='xrayflux',
            old_name='etype',
            new_name='xtype',
        ),
        migrations.AlterField(
            model_name='etype',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ptype',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='xtype',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
