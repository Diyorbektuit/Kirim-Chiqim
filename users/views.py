from .serializers import TgUsersSerializer
from rest_framework import generics, permissions
from .models import TgUsers


class TgUsersCreate(generics.CreateAPIView):
    serializer_class = TgUsersSerializer
    queryset = TgUsers.objects.all()
    permission_classes = [permissions.AllowAny]


class TgUserList(generics.ListAPIView):
    serializer_class = TgUsersSerializer
    queryset = TgUsers.objects.all()
    permission_classes = [permissions.AllowAny]





