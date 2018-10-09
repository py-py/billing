from rest_framework import serializers

from backend.models import Address, StreetType
from backend_rest.serializers import BaseModelSerializer

__all__ = ('AddressSerializer', 'StreetTypeSerializer', )


class StreetTypeSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = StreetType


class AddressSerializer(BaseModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta(BaseModelSerializer.Meta):
        model = Address

    def get_name(self, obj):
        return str(obj)
