from django.conf.urls import include, url
from api.views import ManufacturerViewSet, ShoeColorViewSet, ShoeTypeViewSet, ShoeViewSet
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'manufacturer', ManufacturerViewSet)
router.register(r'color', ShoeColorViewSet)
router.register(r'type', ShoeTypeViewSet)
router.register(r'shoe', ShoeViewSet)


urlpatterns = [
    url(r"^api/", include(router.urls))
]
