from rest_framework.serializers import ModelSerializer, Serializer, IntegerField
from .models import Kirimlar, Chiqimlar



class KirimlarSerializer(ModelSerializer):
    class Meta:
        model = Kirimlar
        fields = (
            'user',
            'name',
            'cost',
            'date'
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
            'date'
        )


class ChiqimlarSumSerializer(Serializer):
    total_cost = IntegerField()