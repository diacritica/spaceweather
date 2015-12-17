from django.contrib.auth import get_user_model
from django.http import HttpResponse

from rest_framework import authentication, permissions, viewsets, filters

from .forms import ProtonfluxFilter, ElectronfluxFilter, XrayfluxFilter
from .forms import SunspotFilter, SunspotregionFilter
from .forms import AlertFilter
from .forms import ImagechannelFilter
from .forms import SolarradiationFilter
from .forms import RadioblackoutFilter
from .forms import GeomagactivityFilter
from .forms import SolarwindFilter
from .forms import ForecastrationaleFilter

from .models import Protonflux, Ptype, Electronflux, Etype, Xrayflux, Xtype
from .models import Sunspot, Sunspottype, Sunspotregion
from .models import Alert, Alerttype
from .models import Imagechannel, Channeltype
from .models import Solarradiation, Solarradiationtype
from .models import Radioblackout, Radioblackouttype
from .models import Geomagactivity
from .models import Solarwind
from .models import Forecastrationale

from .serializers import ProtonfluxSerializer, PtypeSerializer, ElectronfluxSerializer, EtypeSerializer, XrayfluxSerializer, XtypeSerializer
from .serializers import SunspotSerializer, SunspottypeSerializer, SunspotregionSerializer
from .serializers import AlertSerializer, AlerttypeSerializer
from .serializers import ImagechannelSerializer, ChanneltypeSerializer
from .serializers import SolarradiationSerializer, SolarradiationtypeSerializer
from .serializers import RadioblackoutSerializer, RadioblackouttypeSerializer
from .serializers import GeomagactivitySerializer
from .serializers import SolarwindSerializer
from .serializers import ForecastrationaleSerializer

User = get_user_model()

def servefiles(request, file):

    image = open("images/{}".format(file),'rb')
    return HttpResponse(image, content_type='image/gif')

class DefaultsMixin(object):

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )

    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100

    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )

class ProtonfluxViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Protonflux."""

    queryset = Protonflux.objects.order_by('date')
    serializer_class = ProtonfluxSerializer
    filter_class = ProtonfluxFilter
    search_fields = ('date',)
    ordering_fields = ('date', 'value',)

class PtypeViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Ptypes."""

    queryset = Ptype.objects.order_by('name')
    serializer_class = PtypeSerializer
    search_fields = ('name',)
    ordering_fields = ('name',)


class ElectronfluxViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Electronflux."""

    queryset = Electronflux.objects.order_by('date')
    serializer_class = ElectronfluxSerializer
    filter_class = ElectronfluxFilter
    search_fields = ('date',)
    ordering_fields = ('date', 'value',)

class EtypeViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Etypes."""

    queryset = Etype.objects.order_by('name')
    serializer_class = EtypeSerializer
    search_fields = ('name',)
    ordering_fields = ('name',)

class XrayfluxViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Xrayflux."""

    queryset = Xrayflux.objects.order_by('date')
    serializer_class = XrayfluxSerializer
    filter_class = XrayfluxFilter
    search_fields = ('date',)
    ordering_fields = ('date', 'value',)

class XtypeViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Xtypes."""

    queryset = Xtype.objects.order_by('name')
    serializer_class = XtypeSerializer
    search_fields = ('name',)
    ordering_fields = ('name',)

class SunspotViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Sunspots."""

    queryset = Sunspot.objects.order_by('date')
    serializer_class = SunspotSerializer
    filter_class = SunspotFilter
    search_fields = ('date',)
    ordering_fields = ('date', 'value',)

class SunspottypeViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Sunspottypes."""

    queryset = Sunspottype.objects.order_by('name')
    serializer_class = SunspottypeSerializer
    search_fields = ('name',)
    ordering_fields = ('name',)

class SunspotregionViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Sunspot Regions."""

    queryset = Sunspotregion.objects.order_by('date')
    serializer_class = SunspotregionSerializer
    filter_class = SunspotregionFilter
    search_fields = ('date',)
    ordering_fields = ('date', 'region',)

class AlerttypeViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Alerttypes."""

    queryset = Alerttype.objects.order_by('name')
    serializer_class = AlerttypeSerializer
    search_fields = ('name',)
    ordering_fields = ('name',)

class AlertViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Alerts."""

    queryset = Alert.objects.order_by('issuetime')
    serializer_class = AlertSerializer
    filter_class = AlertFilter
    search_fields = ('issuetime',)
    ordering_fields = ('issuetime', 'name',)

class ChanneltypeViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Channeltypes."""

    queryset = Channeltype.objects.order_by('name')
    serializer_class = ChanneltypeSerializer
    search_fields = ('name',)
    ordering_fields = ('name',)

class ImagechannelViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Imagechannel."""

    queryset = Imagechannel.objects.order_by('date')
    serializer_class = ImagechannelSerializer
    filter_class = ImagechannelFilter
    search_fields = ('date',)
    ordering_fields = ('date', 'channeltype',)

class SolarradiationViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Solarradiations."""

    queryset = Solarradiation.objects.order_by('date')
    serializer_class = SolarradiationSerializer
    filter_class = SolarradiationFilter
    search_fields = ('date',)
    ordering_fields = ('date', 'solarradiationtype',)

class SolarradiationtypeViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Solarradiationtypes."""

    queryset = Solarradiationtype.objects.order_by('name')
    serializer_class = SolarradiationtypeSerializer
    search_fields = ('name',)
    ordering_fields = ('name',)

class RadioblackoutViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Radioblackouts."""

    queryset = Radioblackout.objects.order_by('date')
    serializer_class = RadioblackoutSerializer
    filter_class = RadioblackoutFilter
    search_fields = ('date',)
    ordering_fields = ('date', 'radioblackouttype',)

class RadioblackouttypeViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Radioblackouttypes."""

    queryset = Radioblackouttype.objects.order_by('name')
    serializer_class = RadioblackouttypeSerializer
    search_fields = ('name',)
    ordering_fields = ('name',)

class GeomagactivityViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Geomagactivity."""

    queryset = Geomagactivity.objects.order_by('date')
    serializer_class = GeomagactivitySerializer
    filter_class = GeomagactivityFilter
    search_fields = ('date',)
    ordering_fields = ('date',)

class SolarwindViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Solarwind."""

    queryset = Solarwind.objects.order_by('date')
    serializer_class = SolarwindSerializer
    filter_class = SolarwindFilter
    search_fields = ('date',)
    ordering_fields = ('date',)

class ForecastrationaleViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Solarwind."""

    queryset = Forecastrationale.objects.order_by('date')
    serializer_class = ForecastrationaleSerializer
    filter_class = ForecastrationaleFilter
    search_fields = ('date',)
    ordering_fields = ('date',)
