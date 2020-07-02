from rest_framework import serializers
from products.models import Product , Category

#Converter objetos python para json(ou qualquer objeto) e json(qualquer objeto) para python

class ProductModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['id', 'name', 'description','price', 'category']


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        
