from django.contrib.auth import get_user_model

from rest_framework import serializers

from rest_framework.reverse import reverse
from .models import Protonflux, Electronflux, Xrayflux, Ptype, Etype, Xtype

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
