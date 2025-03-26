from django.shortcuts import render
from rest_framework import viewsets
from .models import Coffin, Order
from .serializers import CoffinSerializer, OrderSerializer

# Create your views here.
class CoffinViewSet(viewsets.ModelViewSet):
    queryset = Coffin.objects.all()
    serializer_class = CoffinSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)