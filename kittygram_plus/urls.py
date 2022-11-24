from django.urls import include, path

from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, OwnerViewSet


router = DefaultRouter()
router.register('cats', CatViewSet, basename='cats')
router.register('owners', OwnerViewSet, basename='owners')

urlpatterns = [
    path('', include(router.urls)),
]