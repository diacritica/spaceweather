from django.contrib.auth import get_user_model

from rest_framework import authentication, permissions, viewsets, filters

from .forms import ProtonfluxFilter, ElectronfluxFilter

from .models import Protonflux, Ptype, Electronflux, Etype
from .serializers import ProtonfluxSerializer, PtypeSerializer, ElectronfluxSerializer, EtypeSerializer

User = get_user_model()

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
    """API endpoint for listing and creating Protonflux."""

    queryset = Electronflux.objects.order_by('date')
    serializer_class = ElectronfluxSerializer
    filter_class = ElectronfluxFilter
    search_fields = ('date',)
    ordering_fields = ('date', 'value',)

class EtypeViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Ptypes."""

    queryset = Etype.objects.order_by('name')
    serializer_class = EtypeSerializer
    search_fields = ('name',)
    ordering_fields = ('name',)
