import django_filters

from .models import Protonflux, Ptype


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
