import django_filters

from .models import Protonflux, Ptype, Electronflux, Etype, Xrayflux, Xtype
from .models import Sunspot, Sunspottype, Sunspotregion
from .models import Alert, Alerttype


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
