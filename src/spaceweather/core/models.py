from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Ptype(models.Model):
    
    name = models.CharField(max_length=20, blank=False)
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
    ptype = models.ForeignKey('Ptype', null=True)
    value = models.FloatField(blank=False)
    units = models.CharField(max_length=50, blank=True, default='Protons/cm2-s-sr')
    bogus = models.BooleanField(default=False)

    def __str__(self):
        return "{}:{} {} protonflux".format(self.date,self.ptype.name,self.value)
