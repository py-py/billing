from rest_framework import routers

from backend_rest.views import AddressViewSet, StreetTypeViewSet

router = routers.SimpleRouter()
router.register('address', AddressViewSet)
router.register('streettype', StreetTypeViewSet)

urlpatterns = router.urls