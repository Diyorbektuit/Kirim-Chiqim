#from rest_framework import generics, permissions, status
#from rest_framework.response import Response
#from rest_framework.views import APIView
#from harajat.models import Products
#from harajat.serializers import ProductsSerializer
#
#
#class ProductsList(APIView):
#
#    #permission_classes = [permissions.IsAuthenticated]
#
#    def get(self, request, *args, **kwargs):
#        total_product_data = Products.kunlik_products()
#        serializer = ProductsSerializer(total_product_data)
#        return Response(serializer.data, status=status.HTTP_200_OK)
#
#
