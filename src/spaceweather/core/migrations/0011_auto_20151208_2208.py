# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20151208_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sunspot',
            name='sunspottype',
            field=models.ForeignKey(to='core.Sunspottype'),
        ),
    ]
