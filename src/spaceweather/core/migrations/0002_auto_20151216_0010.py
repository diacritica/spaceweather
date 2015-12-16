# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagechannel',
            name='sdatemax',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='imagechannel',
            name='sdatemin',
            field=models.DateTimeField(blank=True),
        ),
    ]
