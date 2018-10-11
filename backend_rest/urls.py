from rest_framework import routers
from django.conf import settings
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from backend_rest.views import AddressViewSet, StreetTypeViewSet

router = routers.SimpleRouter()
router.register('address', AddressViewSet)
router.register('streettype', StreetTypeViewSet)

urlpatterns = router.urls

if settings.DEBUG:
    schema_view = get_swagger_view(title='Invoice API')
    urlpatterns = [
        path('docs', schema_view)
    ]
