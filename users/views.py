from .serializers import UserRegistrationSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User
# Create your views here.


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]




