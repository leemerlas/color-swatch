from django.urls import include, path
from django.conf.urls import url, include

from rest_framework import routers, urlpatterns

from swatch_api.views import RGBSwatchViewSet, HSLSwatchViewSet, SwatchView

router = routers.DefaultRouter()
router.register(r'rgb', RGBSwatchViewSet)
router.register(r'hsl', HSLSwatchViewSet)
# router.register(r'swatches', SwatchView, base_name='swatch-view')

urlpatterns = [
    path('', include(router.urls)),
    path('swatches/', SwatchView.as_view())
]