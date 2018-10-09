from rest_framework import viewsets

from backend.models import Address, StreetType
from backend_rest.serializers import AddressSerializer, StreetTypeSerializer

class StreetTypeViewSet(viewsets.ModelViewSet):
    serializer_class = StreetTypeSerializer
    queryset = StreetType.objects.all()

class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()