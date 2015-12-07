# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151207_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protonflux',
            name='ptype',
            field=models.ForeignKey(null=True, to='core.Ptype'),
        ),
    ]
