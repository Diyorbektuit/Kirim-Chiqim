from rest_framework.serializers import ModelSerializer, Serializer, IntegerField
from .models import Kirimlar, Chiqimlar
from rest_framework import serializers
from datetime import datetime


#class HourlyCountSerializer(Serializer):
#    hour = serializers.IntegerField()
#    count = IntegerField()
#
#
#class ProductsSerializer(Serializer):
#    total_products = IntegerField()
#    clock_total = HourlyCountSerializer(many=True)


class KirimlarSerializer(ModelSerializer):
    class Meta:
        model = Kirimlar
        fields = (
            'user',
            'name',
            'cost',
        )


class KirimlarSumSerializer(Serializer):
    total_cost = IntegerField()


class ChiqimlarSerializer(ModelSerializer):
    class Meta:
        model = Chiqimlar
        fields = (
            'user',
            'name',
            'cost',
        )


class ChiqimlarSumSerializer(Serializer):
    total_cost = IntegerField()