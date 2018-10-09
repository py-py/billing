from rest_framework import routers

from backend_rest.views import AddressViewSet, StreetTypeViewSet

router = routers.SimpleRouter()
router.register('address', AddressViewSet)
router.register('streettype', StreetTypeViewSet)

urlpatterns = router.urls


from django.urls import path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Invoice API')

urlpatterns += [
    path('docs', schema_view)
]
