'''
from rest_framework import serializers

from api.models import Lambda


class LambdaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lambda
        fields = ['question']

'''