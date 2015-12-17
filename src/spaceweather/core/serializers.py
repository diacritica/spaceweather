from django.contrib.auth import get_user_model

from rest_framework import serializers

from rest_framework.reverse import reverse
from .models import Protonflux, Electronflux, Xrayflux, Ptype, Etype, Xtype
from .models import Sunspot, Sunspottype, Sunspotregion
from .models import Alert, Alerttype
from .models import Imagechannel, Channeltype
from .models import Solarradiation, Solarradiationtype
from .models import Radioblackout, Radioblackouttype
from .models import Geomagactivity
from .models import Solarwind
from .models import Forecastrationale

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active', )

class PtypeSerializer(serializers.ModelSerializer):


    links = serializers.SerializerMethodField()

    class Meta:
        model = Ptype
        fields = ('id', 'name', 'description', 'explanation', 'url', 'origin', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('ptype-detail',
            kwargs={'pk':obj.pk}, request=request),
        }


class EtypeSerializer(serializers.ModelSerializer):


    links = serializers.SerializerMethodField()

    class Meta:
        model = Etype
        fields = ('id', 'name', 'description', 'explanation', 'url', 'origin', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('etype-detail',
            kwargs={'pk':obj.pk}, request=request),
        }

class XtypeSerializer(serializers.ModelSerializer):


    links = serializers.SerializerMethodField()

    class Meta:
        model = Xtype
        fields = ('id', 'name', 'description', 'explanation', 'url', 'origin', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('xtype-detail',
            kwargs={'pk':obj.pk}, request=request),
        }

class SunspottypeSerializer(serializers.ModelSerializer):


    links = serializers.SerializerMethodField()

    class Meta:
        model = Sunspottype
        fields = ('id', 'name', 'description', 'explanation', 'url', 'origin', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('sunspottype-detail',
            kwargs={'pk':obj.pk}, request=request),
        }

class ProtonfluxSerializer(serializers.ModelSerializer):


    links = serializers.SerializerMethodField()
    #ptype = serializers.StringRelatedField()

    class Meta:
        model = Protonflux
        fields = ('id', 'date', 'ptype', 'value', 'units', 'bogus', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('protonflux-detail',
            kwargs={'pk':obj.pk}, request=request),
        }


class ElectronfluxSerializer(serializers.ModelSerializer):


    links = serializers.SerializerMethodField()
    #etype = serializers.StringRelatedField()

    class Meta:
        model = Electronflux
        fields = ('id', 'date', 'etype', 'value', 'units', 'bogus', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('electronflux-detail',
            kwargs={'pk':obj.pk}, request=request),
        }


class XrayfluxSerializer(serializers.ModelSerializer):


    links = serializers.SerializerMethodField()
    #etype = serializers.StringRelatedField()

    class Meta:
        model = Xrayflux
        fields = ('id', 'date', 'xtype', 'value', 'units', 'bogus', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('xrayflux-detail',
            kwargs={'pk':obj.pk}, request=request),
        }

class SunspotSerializer(serializers.ModelSerializer):


    links = serializers.SerializerMethodField()
    #etype = serializers.StringRelatedField()

    class Meta:
        model = Sunspot
        fields = ('id', 'date', 'sunspottype', 'value', 'units', 'bogus', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('sunspot-detail',
            kwargs={'pk':obj.pk}, request=request),
        }

class SunspotregionSerializer(serializers.ModelSerializer):


    links = serializers.SerializerMethodField()
    #etype = serializers.StringRelatedField()

    class Meta:
        model = Sunspotregion
        fields = ('id', 'date', 'region', 'numberofsunspots', 'magneticclass', 'size', 'spotclass', 'location', 'bogus', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('sunspotregion-detail',
            kwargs={'pk':obj.pk}, request=request),
        }


class AlerttypeSerializer(serializers.ModelSerializer):


    links = serializers.SerializerMethodField()

    class Meta:
        model = Alerttype
        fields = ('id', 'name', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('alerttype-detail',
            kwargs={'pk':obj.pk}, request=request),
        }

class AlertSerializer(serializers.ModelSerializer):


    links = serializers.SerializerMethodField()
    #etype = serializers.StringRelatedField()

    class Meta:
        model = Alert
        fields = ('id', 'SWMC', 'serialnumber', 'issuetime', 'alerttype', 'message', 'payload', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('alert-detail',
            kwargs={'pk':obj.pk}, request=request),
        }

class ChanneltypeSerializer(serializers.ModelSerializer):


    links = serializers.SerializerMethodField()

    class Meta:
        model = Channeltype
        fields = ('id', 'name', 'description', 'explanation', 'interval', 'url', 'origin', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('channeltype-detail',
            kwargs={'pk':obj.pk}, request=request),
        }

class ImagechannelSerializer(serializers.ModelSerializer):


    links = serializers.SerializerMethodField()
    #etype = serializers.StringRelatedField()

    class Meta:
        model = Imagechannel
        fields = ('id', 'date', 'channeltype', 'originaldate', 'image', 'bogus', 'sdatemin', 'sdatemax', 'links', )
        readonly_fields = ('image')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('imagechannel-detail',
            kwargs={'pk':obj.pk}, request=request),
        }

class SolarradiationSerializer(serializers.ModelSerializer):


    links = serializers.SerializerMethodField()
    #etype = serializers.StringRelatedField()

    class Meta:
        model = Solarradiation
        fields = ('id', 'date', 'solarradiationtype', 'value', 'bogus',  'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('solarradiation-detail',
            kwargs={'pk':obj.pk}, request=request),
        }

class SolarradiationtypeSerializer(serializers.ModelSerializer):


    links = serializers.SerializerMethodField()
    #etype = serializers.StringRelatedField()

    class Meta:
        model = Solarradiationtype
        fields = ('id', 'name', 'description', 'explanation', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('solarradiationtype-detail',
            kwargs={'pk':obj.pk}, request=request),
        }

class RadioblackoutSerializer(serializers.ModelSerializer):


    links = serializers.SerializerMethodField()
    #etype = serializers.StringRelatedField()

    class Meta:
        model = Radioblackout
        fields = ('id', 'date', 'radioblackouttype', 'value', 'bogus',  'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('radioblackout-detail',
            kwargs={'pk':obj.pk}, request=request),
        }


class RadioblackouttypeSerializer(serializers.ModelSerializer):


    links = serializers.SerializerMethodField()
    #etype = serializers.StringRelatedField()

    class Meta:
        model = Radioblackouttype
        fields = ('id', 'name', 'description', 'explanation', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('radioblackouttype-detail',
            kwargs={'pk':obj.pk}, request=request),
        }

class GeomagactivitySerializer(serializers.ModelSerializer):


    links = serializers.SerializerMethodField()
    #etype = serializers.StringRelatedField()

    class Meta:
        model = Geomagactivity
        fields = ('id', 'date', 'value', 'bogus', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('geomagactivity-detail',
            kwargs={'pk':obj.pk}, request=request),
        }

class ForecastrationaleSerializer(serializers.ModelSerializer):


    links = serializers.SerializerMethodField()
    #etype = serializers.StringRelatedField()

    class Meta:
        model = Forecastrationale
        fields = ('id', 'date', 'radioblackout', 'solarradiation', 'geomagactivity','links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('forecastrationale-detail',
            kwargs={'pk':obj.pk}, request=request),
        }


class SolarwindSerializer(serializers.ModelSerializer):


    links = serializers.SerializerMethodField()
    #etype = serializers.StringRelatedField()

    class Meta:
        model = Solarwind
        fields = ('id', 'date', 'density', 'radialspeed', 'temperature', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('solarwind-detail',
            kwargs={'pk':obj.pk}, request=request),
        }
