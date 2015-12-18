from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from datetime import timedelta

class Ptype(models.Model):

    name = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=True)
    explanation = models.TextField(blank=True)
    url = models.URLField(blank=True)
    origin = models.TextField(blank=True)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name


class Etype(models.Model):

    name = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=True)
    explanation = models.TextField(blank=True)
    url = models.URLField(blank=True)
    origin = models.TextField(blank=True)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

class Xtype(models.Model):

    name = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=True)
    explanation = models.TextField(blank=True)
    url = models.URLField(blank=True)
    origin = models.TextField(blank=True)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

class Sunspottype(models.Model):

    name = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=True)
    explanation = models.TextField(blank=True)
    url = models.URLField(blank=True)
    origin = models.TextField(blank=True)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name



class Protonflux(models.Model):
    """Proton flux"""

    date = models.DateTimeField(unique=False)
    ptype = models.ForeignKey('Ptype', null=False)
    value = models.FloatField(blank=False)
    units = models.CharField(max_length=50, blank=True, default='Protons/cm2-s-sr')
    bogus = models.BooleanField(default=False)

    def __str__(self):
        return "{}:{} {} protonflux".format(self.date, self.ptype.name, self.value)


class Electronflux(models.Model):
    """Electron flux"""

    date = models.DateTimeField(unique=False)
    etype = models.ForeignKey('Etype', null=False)
    value = models.FloatField(blank=False)
    units = models.CharField(max_length=50, blank=True, default='Electrons/cm2-s-sr')
    bogus = models.BooleanField(default=False)

    def __str__(self):
        return "{}:{} {} electronflux".format(self.date, self.etype.name, self.value)

class Xrayflux(models.Model):
    """Xray flux"""

    date = models.DateTimeField(unique=False)
    xtype = models.ForeignKey('Xtype', null=False)
    value = models.FloatField(blank=False)
    units = models.CharField(max_length=50, blank=True, default='Watt/m2')
    bogus = models.BooleanField(default=False)

    def __str__(self):
        return "{}:{} {} xrayflux".format(self.date, self.xtype.name, self.value)

class Sunspot(models.Model):
    """Sunspot number"""

    date = models.DateField(unique=False)
    sunspottype = models.ForeignKey('Sunspottype', null=False)
    value = models.FloatField(blank=False)
    units = models.CharField(max_length=50, blank=True, default='sunspots')
    bogus = models.BooleanField(default=False)


    def __str__(self):
        return "{}:{} {} sunspots".format(self.date, self.sunspottype.name, self.value)

class Sunspotregion(models.Model):
    """Sunspot Regions"""

    MAGNETIC_CLASS_CHOICES = (
        ('α',_('Alpha: A unipolar sunspot group')),
        ('β',_('Bèta: A sunspot group that has a positive and a negative polarity (or bipolar) with a simple division between the polarities')),
        ('γ',_('Gamma: A complex region in which the positive and negative polarities are so irregularly distributed that they cannot be classified as a bipolar Sunspot group')),
        ('β-γ',_('Bèta-Gamma: A bipolar sunspot group but complex enough so that no line can be drawn between spots of opposite polarity')),
        ('δ',('Delta: The umbrae of opposite polarity in a single penumbra')),
        ('β-δ',_('Bèta-Delta: A sunspot group with a general beta magnetic configuration but contains one (or more) delta sunspots')),
        ('β-γ-δ',_('Bèta-Gamma-Delta: A sunspot group with a beta-gamma magnetic configuration but contains one (or more) delta sunspots')),
        ('γ-δ',_('Gamma-Delta: A sunspot group with a gamma magnetic configuration but contains one (or more) delta sunspots')),
    )

    date = models.DateField(unique=False)
    region = models.IntegerField(blank=False)
    numberofsunspots = models.IntegerField(blank=False)
    size = models.SmallIntegerField(blank=False)
    magneticclass = models.CharField(max_length=10, choices=MAGNETIC_CLASS_CHOICES, default='α')
    spotclass = models.CharField(max_length=4)
    location = models.CharField(max_length=6)
    bogus = models.BooleanField(default=False)


    def __str__(self):
        return "{}:{} {} sunspot region".format(self.region, self.date, self.numberofsunspots)


class Alerttype(models.Model):

    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name


class Alert(models.Model):
    """Alert"""

    SWMC_CHOICES = (
        ('ALTXMF',_('X-ray Flux exceeded M5')),
        ('SUMX01',_('X-ray Event exceeded M5 (thresholds: M5 , X1, X10, or X20)')),
        ('ALTTP2',_('Type II Radio Emission')),
        ('ALTTP4',_('Type IV Radio Emission')),
        ('SUM10R',('10cm Radio Burst')),
        ('WARSUD',_('Geomagnetic Sudden Impulse expected')),
        ('SUMSUD',_('Geomagnetic Sudden Impulse')),
        ('WATA20',_('Geomagnetic Storm Category G1 Predicted')),
        ('WATA50',_('Geomagnetic Storm Category (G1, G2, G3, G4 or greater) predicted')),
        ('WARK04',_('Geomagnetic K-index of 4 expected')),
        ('WARK05',_('Geomagnetic K-index of 5 expected')),
        ('WARK06',_('Geomagnetic K-index of 6 expected')),
        ('WARK07',_('Geomagnetic K-index of 7 or greater expected')),
        ('ALTK04',_('Geomagnetic K-index of 4')),
        ('ALTK05',_('Geomagnetic K-index of 5')),
        ('ALTK06',_('Geomagnetic K-index of 6')),
        ('ALTK07',_('Geomagnetic K-index of 7')),
        ('ALTK08',_('Geomagnetic K-index of 8')),
        ('ALTK09',_('Geomagnetic K-index of 9')),
        ('ALTEF3',_('Electron 2MeV Integral Flux exceeded 1000pfu')),
        ('WARPX1',_('Proton 10MeV Integral Flux above 10pfu expected')),
        ('ALTPX1',_('Proton Event 10MeV Integral Flux exceeded threshold PX1=10, PX2=100, PX3=1000, PX4=10000, or PX5=100000pfu')),
        ('SUMPX4',_('Proton Event 10MeV Integral Flux exceeded 10pfu threshold PX1=10, PX2=100, PX3=1000, PX4=10000, or PX5=100000pfu')),
        ('WARPX1',_('Proton 10MeV Integral Flux above 10pfu expected')),
        ('WARPC0',_('Proton 100MeV Integral Flux above 1pfu expected')),
        ('ALTPC0',_('Proton Event 100MeV Integral Flux exceeded 1pfu')),
        ('SUMPC0',_('Proton Event 100MeV Integral Flux exceeded 1pfu')),
    )

    SWMC = models.CharField(max_length=10, choices=SWMC_CHOICES)
    serialnumber = models.IntegerField(blank=False)
    issuetime = models.DateTimeField(blank=False)
    alerttype = models.ForeignKey('Alerttype', null=False)
    message = models.TextField(max_length=500)
    payload = models.TextField(max_length=1000)

    def __str__(self):
        return "{}:{} {} alert".format(self.SWMC, self.serialnumber, self.issuetime)

class Imagechannel(models.Model):

    date = models.DateTimeField(unique=False)
    channeltype = models.ForeignKey('Channeltype', null=False)
    originaldate = models.DateTimeField(unique=False)
    image = models.ImageField(upload_to="images", blank=True)
    bogus = models.BooleanField(default=False)
    sdatemax = models.DateTimeField(blank=True, unique=False)
    sdatemin = models.DateTimeField(blank=True, unique=False)

    def save(self, *args, **kwargs):
        td = timedelta(minutes=self.channeltype.interval)
        print(td)
        self.sdatemin = self.originaldate# - td
        self.sdatemax = self.originaldate# + td
        super(Imagechannel, self).save(*args, **kwargs)


    def __str__(self):
        return "{}:{} {} imagechannel".format(self.date, self.channeltype.name, self.originaldate)

class Channeltype(models.Model):

    name = models.CharField(max_length=50, blank=False)
    interval = models.SmallIntegerField(blank=False)
    description = models.TextField(blank=True)
    explanation = models.TextField(blank=True)
    url = models.URLField(blank=True)
    origin = models.TextField(blank=True)

    def __str__(self):
        return "{}:{} channeltype".format(self.name, self.interval)

class Solarradiationtype(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    explanation = models.TextField(blank=True)
    url = models.URLField(blank=True)
    origin = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Solarradiation(models.Model):

    date = models.DateField(unique=False)
    solarradiationtype = models.ForeignKey('Solarradiationtype', null=False)
    value = models.SmallIntegerField(blank=True)
    bogus = models.BooleanField(default=False)


class Radioblackouttype(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    explanation = models.TextField(blank=True)
    url = models.URLField(blank=True)
    origin = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Radioblackout(models.Model):

    date = models.DateField(unique=False)
    radioblackouttype = models.ForeignKey('Radioblackouttype', null=False)
    value = models.SmallIntegerField(blank=True)
    bogus = models.BooleanField(default=False)
