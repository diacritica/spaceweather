# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20151211_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('SWMC', models.CharField(max_length=10, choices=[('ALTXMF', 'X-ray Flux exceeded M5'), ('SUMX01', 'X-ray Event exceeded M5 (thresholds: M5 , X1, X10, or X20)'), ('ALTTP2', 'Type II Radio Emission'), ('ALTTP4', 'Type IV Radio Emission'), ('SUM10R', '10cm Radio Burst'), ('WARSUD', 'Geomagnetic Sudden Impulse expected'), ('SUMSUD', 'Geomagnetic Sudden Impulse'), ('WATA50', 'Geomagnetic K-index of (thresholds 4, 5, 6, or "7 or greater") expected'), ('WARK05', 'Geomagnetic K-index of (thresholds 4, 5, 6, or "7 or greater") expected'), ('ALTK05', 'Geomagnetic K-index of (thresholds 4 , 5, 6, 7, 8, or 9)'), ('ALTEF3', 'Electron 2MeV Integral Flux exceeded 1000pfu'), ('WARPX1', 'Proton 10MeV Integral Flux above 10pfu expected'), ('ALTPX1', 'Proton Event 10MeV Integral Flux exceeded threshold PX1=10, PX2=100, PX3=1000, PX4=10000, or PX5=100000pfu'), ('SUMPX4', 'Proton Event 10MeV Integral Flux exceeded 10pfu threshold PX1=10, PX2=100, PX3=1000, PX4=10000, or PX5=100000pfu'), ('WARPX1', 'Proton 10MeV Integral Flux above 10pfu expected'), ('WARPC0', 'Proton 100MeV Integral Flux above 1pfu expected'), ('ALTPC0', 'Proton Event 100MeV Integral Flux exceeded 1pfu'), ('SUMPC0', 'Proton Event 100MeV Integral Flux exceeded 1pfu')])),
                ('serialnumber', models.IntegerField()),
                ('issuetime', models.DateTimeField()),
                ('message', models.TextField(max_length=500)),
                ('payload', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Alerttype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='sunspot',
            name='sunspottype',
            field=models.ForeignKey(to='core.Sunspottype'),
        ),
        migrations.AddField(
            model_name='alert',
            name='alerttype',
            field=models.ForeignKey(to='core.Alerttype'),
        ),
    ]
