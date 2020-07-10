
from rest_framework import serializers

from .models import Lambda

#Forma como representar os dados
class LambdaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lambda
        fields = ['question', 'solution']
