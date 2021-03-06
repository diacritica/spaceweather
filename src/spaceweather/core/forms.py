import django_filters

from .models import Protonflux, Ptype, Electronflux, Etype, Xrayflux, Xtype
from .models import Sunspot, Sunspottype, Sunspotregion
from .models import Alert, Alerttype
from .models import Channeltype, Imagechannel
from .models import Solarradiation, Solarradiationtype
from .models import Radioblackout, Radioblackouttype
from .models import Geomagactivity
from .models import Solarwind
from .models import Forecastrationale


class NullFilter(django_filters.BooleanFilter):
    """Filter on a field set as null or not."""

    def filter(self, qs, value):
        if value is not None:
            return qs.filter(**{'%s__isnull' % self.name: value})
        return qs


class ProtonfluxFilter(django_filters.FilterSet):

    noptype = NullFilter(name='ptype')
    date_min = django_filters.DateFilter(name='date',lookup_type='gte')
    date_max = django_filters.DateFilter(name='date',lookup_type='lte')

    class Meta:
        model = Protonflux
        fields = ('date_min', 'date_max', 'date', 'ptype', 'bogus', )


class ElectronfluxFilter(django_filters.FilterSet):

    noetype = NullFilter(name='etype')
    date_min = django_filters.DateFilter(name='date',lookup_type='gte')
    date_max = django_filters.DateFilter(name='date',lookup_type='lte')

    class Meta:
        model = Electronflux
        fields = ('date_min', 'date_max', 'date', 'etype', 'bogus', )

class XrayfluxFilter(django_filters.FilterSet):

    noxtype = NullFilter(name='xtype')
    date_min = django_filters.DateFilter(name='date',lookup_type='gte')
    date_max = django_filters.DateFilter(name='date',lookup_type='lte')

    class Meta:
        model = Xrayflux
        fields = ('date_min', 'date_max', 'date', 'xtype', 'bogus', )

class SunspotFilter(django_filters.FilterSet):

    nosunspottype = NullFilter(name='sunspottype')
    date_min = django_filters.DateFilter(name='date',lookup_type='gte')
    date_max = django_filters.DateFilter(name='date',lookup_type='lte')

    class Meta:
        model = Sunspot
        fields = ('date_min', 'date_max', 'date', 'sunspottype', 'bogus', )

class SunspotregionFilter(django_filters.FilterSet):

    date_min = django_filters.DateFilter(name='date',lookup_type='gte')
    date_max = django_filters.DateFilter(name='date',lookup_type='lte')

    class Meta:
        model = Sunspotregion
        fields = ('date_min', 'date_max', 'date', 'region', 'bogus', )


class AlertFilter(django_filters.FilterSet):

    date_min = django_filters.DateFilter(name='issuetime',lookup_type='gte')
    date_max = django_filters.DateFilter(name='issuetime',lookup_type='lte')

    class Meta:
        model = Alert
        fields = ('date_min', 'date_max', 'issuetime', 'alerttype', 'SWMC', )

class ImagechannelFilter(django_filters.FilterSet):

    date_min = django_filters.DateFilter(name='sdatemin',lookup_type='gte')
    date_max = django_filters.DateFilter(name='sdatemax',lookup_type='lte')

    class Meta:
        model = Imagechannel
        fields = ('date_min', 'date_max', 'date', 'channeltype', 'bogus')

class SolarradiationFilter(django_filters.FilterSet):

    date_min = django_filters.DateFilter(name='date',lookup_type='gte')
    date_max = django_filters.DateFilter(name='date',lookup_type='lte')

    class Meta:
        model = Solarradiation
        fields = ('date_min', 'date_max', 'date', 'value', 'solarradiationtype', 'bogus')

class RadioblackoutFilter(django_filters.FilterSet):

    date_min = django_filters.DateFilter(name='date',lookup_type='gte')
    date_max = django_filters.DateFilter(name='date',lookup_type='lte')

    class Meta:
        model = Radioblackout
        fields = ('date_min', 'date_max', 'date', 'value', 'radioblackouttype', 'bogus')

class GeomagactivityFilter(django_filters.FilterSet):

    date_min = django_filters.DateFilter(name='date',lookup_type='gte')
    date_max = django_filters.DateFilter(name='date',lookup_type='lte')

    class Meta:
        model = Geomagactivity
        fields = ('date_min', 'date_max', 'date', 'value', 'bogus')

class SolarwindFilter(django_filters.FilterSet):

    date_min = django_filters.DateFilter(name='date',lookup_type='gte')
    date_max = django_filters.DateFilter(name='date',lookup_type='lte')

    class Meta:
        model = Solarwind
        fields = ('date_min', 'date_max', 'date', 'density', 'radialspeed','temperature', 'bogus')

class ForecastrationaleFilter(django_filters.FilterSet):

    date_min = django_filters.DateFilter(name='date',lookup_type='gte')
    date_max = django_filters.DateFilter(name='date',lookup_type='lte')

    class Meta:
        model = Forecastrationale
        fields = ('date_min', 'date_max', 'date', 'radioblackout','solarradiation','geomagactivity')
