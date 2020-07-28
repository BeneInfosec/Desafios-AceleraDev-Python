from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_api.api_permissions import OnlyAdminCanCreate
from rest_api.serializers import (
    ProductModelSerializer,
    CategoryModelSerializer,
    OrderModelSerializer
)
from products.models import Product, Category, Order

# Create your views here.

#Example 1
class ProductApiViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

#Example 2
class CategoryListOnlyAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

    def get(self, request, *args, **kwargs):
        # validation
        return self.list(request, *args, **kwargs)

#Example 3
class OrderAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, OnlyAdminCanCreate]

    def post(self, request, pk, format=None):
        serializer = OrderModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        if not pk:
            orders = Order.objects.all()
            serializer = OrderModelSerializer(orders, many=True)
        else:
            order = Order.objects.get(pk=pk)
            serializer = OrderModelSerializer(order)

        return Response(serializer.data)
