from django.shortcuts import render

from rest_framework.decorators import api_view
from collections import Counter 
from rest_framework.response import Response

@api_view(['POST'])
def lambda_function(request):
    data = request.data.get('question')
    solution = [item for items, c in Counter(data).most_common() 
                                      for item in [items] * c] 
    return Response({"solution": solution})

