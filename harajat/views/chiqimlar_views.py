from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from harajat.models import Chiqimlar
from harajat.serializers import ChiqimlarSerializer, ChiqimlarSumSerializer


#Crud
class ChiqimlarList(generics.ListAPIView):
    queryset = Chiqimlar.objects.all()
    serializer_class = ChiqimlarSerializer
    permission_classes = []


class ChiqimlarDetail(generics.RetrieveAPIView):
    queryset = Chiqimlar.objects.all()
    serializer_class = ChiqimlarSerializer
    permission_classes = []


class ChiqimlarCreate(generics.CreateAPIView):
    queryset = Chiqimlar.objects.all()
    serializer_class = ChiqimlarSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = ChiqimlarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            self.create(request,  *args, **kwargs)
            return Response(serializer.data)


class ChiqimlarUpdate(generics.UpdateAPIView):
    serializer_class = ChiqimlarSerializer
    permission_classes = []

    def get_queryset(self):
        return Chiqimlar.objects.filter(user=self.request.user)


class ChiqimlarDelete(generics.DestroyAPIView):
    serializer_class = ChiqimlarSerializer
    permission_classes = []

    def get_queryset(self):
        return Chiqimlar.objects.filter(user=self.request.user)


#oylik kunlik hisobot
class KunlikChiqimlarList(generics.ListAPIView):
    serializer_class = ChiqimlarSerializer

    permission_classes = []

    def get_queryset(self):
        return Chiqimlar.kunlik_chiqimlar()


class KunlikChiqimlarUmumiy(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        total_cost = Chiqimlar.kunlik_chiqimlar_umumiy()
        data = {'total_cost': total_cost}
        serializer = ChiqimlarSumSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OylikChiqimlarList(generics.ListAPIView):
    queryset = Chiqimlar.oylik_chiqimalar()
    serializer_class = ChiqimlarSerializer
    permission_classes = []


class OylikChiqimlarUmumiy(APIView):
    permission_classes = []

    def get(self,  request, *args, **kwargs):
        total_cost = Chiqimlar.oylik_chiqimlar_umumiy()
        data = {'total_cost': total_cost}
        serializer = ChiqimlarSumSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

