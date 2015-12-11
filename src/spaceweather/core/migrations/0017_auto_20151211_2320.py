# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20151211_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='SWMC',
            field=models.CharField(max_length=10, choices=[('ALTXMF', 'X-ray Flux exceeded M5'), ('SUMX01', 'X-ray Event exceeded M5 (thresholds: M5 , X1, X10, or X20)'), ('ALTTP2', 'Type II Radio Emission'), ('ALTTP4', 'Type IV Radio Emission'), ('SUM10R', '10cm Radio Burst'), ('WARSUD', 'Geomagnetic Sudden Impulse expected'), ('SUMSUD', 'Geomagnetic Sudden Impulse'), ('WATA50', 'Geomagnetic Storm Category (G1, G2, G3, G4 or greater) predicted'), ('WARK04', 'Geomagnetic K-index of 4 expected'), ('WARK05', 'Geomagnetic K-index of 5 expected'), ('WARK06', 'Geomagnetic K-index of 6 expected'), ('WARK07', 'Geomagnetic K-index of 7 or greater expected'), ('ALTK04', 'Geomagnetic K-index of 4'), ('ALTK05', 'Geomagnetic K-index of 5'), ('ALTK06', 'Geomagnetic K-index of 6'), ('ALTK07', 'Geomagnetic K-index of 7'), ('ALTK08', 'Geomagnetic K-index of 8'), ('ALTK09', 'Geomagnetic K-index of 9'), ('ALTEF3', 'Electron 2MeV Integral Flux exceeded 1000pfu'), ('WARPX1', 'Proton 10MeV Integral Flux above 10pfu expected'), ('ALTPX1', 'Proton Event 10MeV Integral Flux exceeded threshold PX1=10, PX2=100, PX3=1000, PX4=10000, or PX5=100000pfu'), ('SUMPX4', 'Proton Event 10MeV Integral Flux exceeded 10pfu threshold PX1=10, PX2=100, PX3=1000, PX4=10000, or PX5=100000pfu'), ('WARPX1', 'Proton 10MeV Integral Flux above 10pfu expected'), ('WARPC0', 'Proton 100MeV Integral Flux above 1pfu expected'), ('ALTPC0', 'Proton Event 100MeV Integral Flux exceeded 1pfu'), ('SUMPC0', 'Proton Event 100MeV Integral Flux exceeded 1pfu')]),
        ),
        migrations.AlterField(
            model_name='sunspot',
            name='sunspottype',
            field=models.ForeignKey(to='core.Sunspottype'),
        ),
    ]
