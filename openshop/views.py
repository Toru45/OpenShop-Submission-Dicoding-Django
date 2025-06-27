from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ProductSerializer
from .models import OpenShop
from django.http import Http404

class ProductList(APIView):
    def post(self, request):
        note = ProductSerializer(data=request.data, context={'request': request}) 
        if note.is_valid(raise_exception=True):
            note.save()
            return Response(note.data, status=status.HTTP_201_CREATED)
        return Response(note.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        notes = OpenShop.objects.all()
        serializer = ProductSerializer(notes, many=True, context={'request': request})  
        return Response({
            "products": serializer.data
        }, status=status.HTTP_200_OK)

class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return OpenShop.objects.get(pk=pk)
        except OpenShop.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        product = self.get_object(pk)
        product.is_delete = True
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)