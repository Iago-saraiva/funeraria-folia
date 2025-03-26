from rest_framework import serializers
from .models import Coffin, Order

class CoffinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffin
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'