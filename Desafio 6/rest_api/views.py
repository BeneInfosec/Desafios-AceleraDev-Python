from django.shortcuts import render
#Classes misturadas com outras classes para dar o comportamento desejado
from rest_framework import mixins

from rest_framework import generics

from rest_framework import viewsets

from rest_api.serializers import ProductModelsSerializer, CategoryModelSerializer

from products.models import Product , Category


class ProductApiViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelsSerializer

class CategoryListOnlyAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

    #vem do generics
    def get(self, request, *args, **kwargs):
        #Poderia implementar uma validação
        return self.list(request, *args, **kwargs)

