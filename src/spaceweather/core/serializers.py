from django.contrib.auth import get_user_model

from rest_framework import serializers

from rest_framework.reverse import reverse
from .models import Protonflux, Ptype

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


class ProtonfluxSerializer(serializers.ModelSerializer):


    links = serializers.SerializerMethodField()
    ptype = serializers.StringRelatedField()

    class Meta:
        model = Protonflux
        fields = ('id', 'date', 'ptype', 'value', 'units', 'bogus', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('protonflux-detail',
            kwargs={'pk':obj.pk}, request=request),
        }
