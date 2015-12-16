# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('SWMC', models.CharField(max_length=10, choices=[('ALTXMF', 'X-ray Flux exceeded M5'), ('SUMX01', 'X-ray Event exceeded M5 (thresholds: M5 , X1, X10, or X20)'), ('ALTTP2', 'Type II Radio Emission'), ('ALTTP4', 'Type IV Radio Emission'), ('SUM10R', '10cm Radio Burst'), ('WARSUD', 'Geomagnetic Sudden Impulse expected'), ('SUMSUD', 'Geomagnetic Sudden Impulse'), ('WATA20', 'Geomagnetic Storm Category G1 Predicted'), ('WATA50', 'Geomagnetic Storm Category (G1, G2, G3, G4 or greater) predicted'), ('WARK04', 'Geomagnetic K-index of 4 expected'), ('WARK05', 'Geomagnetic K-index of 5 expected'), ('WARK06', 'Geomagnetic K-index of 6 expected'), ('WARK07', 'Geomagnetic K-index of 7 or greater expected'), ('ALTK04', 'Geomagnetic K-index of 4'), ('ALTK05', 'Geomagnetic K-index of 5'), ('ALTK06', 'Geomagnetic K-index of 6'), ('ALTK07', 'Geomagnetic K-index of 7'), ('ALTK08', 'Geomagnetic K-index of 8'), ('ALTK09', 'Geomagnetic K-index of 9'), ('ALTEF3', 'Electron 2MeV Integral Flux exceeded 1000pfu'), ('WARPX1', 'Proton 10MeV Integral Flux above 10pfu expected'), ('ALTPX1', 'Proton Event 10MeV Integral Flux exceeded threshold PX1=10, PX2=100, PX3=1000, PX4=10000, or PX5=100000pfu'), ('SUMPX4', 'Proton Event 10MeV Integral Flux exceeded 10pfu threshold PX1=10, PX2=100, PX3=1000, PX4=10000, or PX5=100000pfu'), ('WARPX1', 'Proton 10MeV Integral Flux above 10pfu expected'), ('WARPC0', 'Proton 100MeV Integral Flux above 1pfu expected'), ('ALTPC0', 'Proton Event 100MeV Integral Flux exceeded 1pfu'), ('SUMPC0', 'Proton Event 100MeV Integral Flux exceeded 1pfu')])),
                ('serialnumber', models.IntegerField()),
                ('issuetime', models.DateTimeField()),
                ('message', models.TextField(max_length=500)),
                ('payload', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Alerttype',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Channeltype',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('interval', models.SmallIntegerField()),
                ('description', models.TextField(blank=True)),
                ('explanation', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('origin', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Electronflux',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date', models.DateTimeField()),
                ('value', models.FloatField()),
                ('units', models.CharField(max_length=50, default='Electrons/cm2-s-sr', blank=True)),
                ('bogus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Etype',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
                ('explanation', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('origin', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Imagechannel',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date', models.DateTimeField()),
                ('originaldate', models.DateTimeField()),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('bogus', models.BooleanField(default=False)),
                ('sdatemax', models.DateTimeField()),
                ('sdatemin', models.DateTimeField()),
                ('channeltype', models.ForeignKey(to='core.Channeltype')),
            ],
        ),
        migrations.CreateModel(
            name='Protonflux',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date', models.DateTimeField()),
                ('value', models.FloatField()),
                ('units', models.CharField(max_length=50, default='Protons/cm2-s-sr', blank=True)),
                ('bogus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ptype',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
                ('explanation', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('origin', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sunspot',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date', models.DateField()),
                ('value', models.FloatField()),
                ('units', models.CharField(max_length=50, default='sunspots', blank=True)),
                ('bogus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sunspotregion',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date', models.DateField()),
                ('region', models.IntegerField()),
                ('numberofsunspots', models.IntegerField()),
                ('size', models.SmallIntegerField()),
                ('magneticclass', models.CharField(max_length=10, default='α', choices=[('α', 'Alpha: A unipolar sunspot group'), ('β', 'Bèta: A sunspot group that has a positive and a negative polarity (or bipolar) with a simple division between the polarities'), ('γ', 'Gamma: A complex region in which the positive and negative polarities are so irregularly distributed that they cannot be classified as a bipolar Sunspot group'), ('β-γ', 'Bèta-Gamma: A bipolar sunspot group but complex enough so that no line can be drawn between spots of opposite polarity'), ('δ', 'Delta: The umbrae of opposite polarity in a single penumbra'), ('β-δ', 'Bèta-Delta: A sunspot group with a general beta magnetic configuration but contains one (or more) delta sunspots'), ('β-γ-δ', 'Bèta-Gamma-Delta: A sunspot group with a beta-gamma magnetic configuration but contains one (or more) delta sunspots'), ('γ-δ', 'Gamma-Delta: A sunspot group with a gamma magnetic configuration but contains one (or more) delta sunspots')])),
                ('spotclass', models.CharField(max_length=4)),
                ('location', models.CharField(max_length=6)),
                ('bogus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sunspottype',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
                ('explanation', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('origin', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Xrayflux',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date', models.DateTimeField()),
                ('value', models.FloatField()),
                ('units', models.CharField(max_length=50, default='Watt/m2', blank=True)),
                ('bogus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Xtype',
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
            model_name='xrayflux',
            name='xtype',
            field=models.ForeignKey(to='core.Xtype'),
        ),
        migrations.AddField(
            model_name='sunspot',
            name='sunspottype',
            field=models.ForeignKey(to='core.Sunspottype'),
        ),
        migrations.AddField(
            model_name='protonflux',
            name='ptype',
            field=models.ForeignKey(to='core.Ptype'),
        ),
        migrations.AddField(
            model_name='electronflux',
            name='etype',
            field=models.ForeignKey(to='core.Etype'),
        ),
        migrations.AddField(
            model_name='alert',
            name='alerttype',
            field=models.ForeignKey(to='core.Alerttype'),
        ),
    ]
