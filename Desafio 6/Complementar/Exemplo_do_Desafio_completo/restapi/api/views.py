from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import LambdaModelSerializer
from collections import Counter 
from .models import Lambda

class LambdaApiViewSet(viewsets.ModelViewSet):
    queryset = Lambda.objects.all()
    serializer_class = LambdaModelSerializer



@api_view(["POST"])
def lambda_function(request):
    
    data=request.data.get('question')
    solution =[item for items, c in Counter(data).most_common()
                  for item in [items] * c]
    return Response({"solution": solution}, status = status.HTTP_201_CREATED)
