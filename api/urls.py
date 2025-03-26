from django.urls import path, include
from rest_framework import routers

from .views import CoffinViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register('coffins', CoffinViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]