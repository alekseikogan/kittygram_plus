from django.urls import include, path

from rest_framework.routers import DefaultRouter
from cats.views import CatViewSet, LightCatViewSet, OwnerViewSet


router = DefaultRouter()
router.register('cats', CatViewSet, basename='cats')
router.register('owners', OwnerViewSet, basename='owners')
router.register(r'mycats', LightCatViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
