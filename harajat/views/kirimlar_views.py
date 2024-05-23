from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from harajat.models import Kirimlar
from harajat.serializers import KirimlarSerializer, KirimlarSumSerializer


# CRUD
class KirimlarList(generics.ListAPIView):
    serializer_class = KirimlarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Kirimlar.objects.filter(user=self.request.user)


class KirimlarDetail(generics.RetrieveAPIView):
    queryset = Kirimlar.objects.all()
    serializer_class = KirimlarSerializer
    permission_classes = [permissions.IsAuthenticated]


class KirimlarCreate(generics.CreateAPIView):
    queryset = Kirimlar.objects.all()
    serializer_class = KirimlarSerializer
    permission_classes = [permissions.IsAuthenticated]


class KirimlarUpdate(generics.UpdateAPIView):
    serializer_class = KirimlarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Kirimlar.objects.filter(user=self.request.user)


class KirimlarDelete(generics.DestroyAPIView):
    serializer_class = KirimlarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Kirimlar.objects.filter(user=self.request.user)


# kunlik oylik hisobot


class BugungiKirimlar(generics.ListAPIView):
    queryset = Kirimlar.kunlik_kirimlar()
    serializer_class = KirimlarSerializer
    permission_classes = [permissions.IsAuthenticated]


class KunlikKirimlarUmumiy(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        total_cost = Kirimlar.kunlik_kirimlar_umumiy()
        data = {'total_cost': total_cost}
        serializer = KirimlarSumSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OylikKirimlar(generics.ListAPIView):
    serializer_class = KirimlarSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Kirimlar.oylik_kirimlar()


class OylikKirimlarSum(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        total_cost = Kirimlar.oylik_kirimlar_umumiy()
        data = {'total_cost': total_cost}
        serializer = KirimlarSumSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
