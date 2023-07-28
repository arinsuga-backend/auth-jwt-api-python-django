from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from ..serializers.user import UserSerializer

# GET Action
def get_action(request):
    serialize = UserSerializer(User.objects.all())
    return Response({
        'method' : 'GET',
        'status' : status.HTTP_200_OK,
        'message' : 'ok',
        'result' : serialize.data,
    })

# POST Action
def post_action(request):
    return Response({ 'data':'POST - Data' })

# PUT Action
def put_action(request):
    return Response({ 'data':'PUT - Data' })

# PATCH Action
def patch_action(request):
    return Response({ 'data':'PATCH - Data' })

# DELETE Action
def delete_action(request):
    return Response({ 'data':'DELETE - Data' })

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def users(request):
    # GET Request
    if request.method == 'GET':
        return get_action(request)

    # POST Request
    if request.method == 'POST':
        return post_action(request)
    
    # PUT Request
    if request.method == 'PUT':
        return put_action(request)
    
    # PATCH Request
    if request.method == 'PATCH':
        return patch_action(request)

    # DELETE Request
    if request.method == 'DELETE':
        return delete_action(request)



