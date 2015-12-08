# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20151208_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='SunspotRegions',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date', models.DateField()),
                ('region', models.IntegerField()),
                ('numberofsunspots', models.IntegerField()),
                ('size', models.SmallIntegerField()),
                ('magneticclass', models.CharField(default='α', choices=[('α', 'Alpha: A unipolar sunspot group'), ('β', 'Bèta: A sunspot group that has a positive and a negative polarity (or bipolar) with a simple division between the polarities'), ('γ', 'Gamma: A complex region in which the positive and negative polarities are so irregularly distributed that they cannot be classified as a bipolar Sunspot group'), ('β-γ', 'Bèta-Gamma: A bipolar sunspot group but complex enough so that no line can be drawn between spots of opposite polarity'), ('δ', 'Delta: The umbrae of opposite polarity in a single penumbra'), ('β-δ', 'Bèta-Delta: A sunspot group with a general beta magnetic configuration but contains one (or more) delta sunspots'), ('β-γ-δ', 'Bèta-Gamma-Delta: A sunspot group with a beta-gamma magnetic configuration but contains one (or more) delta sunspots'), ('γ-δ', 'Gamma-Delta: A sunspot group with a gamma magnetic configuration but contains one (or more) delta sunspots')], max_length=10)),
                ('spotclass', models.CharField(max_length=4)),
                ('location', models.CharField(max_length=6)),
                ('bogus', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='sunspot',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='sunspot',
            name='sunspottype',
            field=models.ForeignKey(to='core.Sunspottype'),
        ),
    ]
