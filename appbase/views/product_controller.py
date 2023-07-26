from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def all(request):
    return Response({
        'data':[
            {'name':'mazda', 'price':500000000},
            {'name':'toyota', 'price':700000000},
            {'name':'honda', 'price':800000000},
        ]
    })