# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20151208_2204'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SunspotRegions',
            new_name='SunspotRegion',
        ),
        migrations.AlterField(
            model_name='sunspot',
            name='sunspottype',
            field=models.ForeignKey(to='core.Sunspottype'),
        ),
    ]
