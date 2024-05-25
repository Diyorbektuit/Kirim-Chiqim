from .models import TgUsers
from rest_framework import serializers


class TgUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUsers
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'tg_id',
        )