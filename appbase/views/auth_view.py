from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def authenticate(request):
    #GET Request
    if request.method == 'GET':
        return get_action(request=request)

    #POST Request
    if request.method == 'POST':
        return post_action(request=request)

    #PUT Request
    if request.method == 'PUT':
        return put_action(request=request)

    #PATCH Request
    if request.method == 'PATCH':
        return patch_action(request=request)
    
    #DELETE Request
    if request.method == 'DELETE':
        return delete_action(request=request)

#GET Action
def get_action(request):
    return Response({
        'method':'GET',
        'code':200,
        'message':'GET - You are authenticated',
        'result': {
            'email':'mail@email.com',
            'name':'John Doe',
            'roles':['staff', 'reporter']
        }
    })

#POST Action
def post_action(request):
    return Response({
        'method':'POST',
        'code':200,
        'message':'POST - You are authenticated',
        'result': {
            'email':'mail@email.com',
            'name':'John Doe',
            'roles':['staff', 'reporter'],
            #'data':  BaseSerializer(data=request.data) 
        }
    })

#PUT Action
def put_action(request):
    return Response({
        'method':'PUT',
        'code':200,
        'message':'PUT - You are authenticated',
        'result': {
            'email':'mail@email.com',
            'name':'John Doe',
            'roles':['staff', 'reporter']
        }
    })

#PATCH Action
def patch_action(request):
    return Response({
        'method':'PATCH',
        'code':200,
        'message':'PATCH - You are authenticated',
        'result': {
            'email':'mail@email.com',
            'name':'John Doe',
            'roles':['staff', 'reporter']
        }
    })

#DELETE Action
def delete_action(request):
    return Response({
        'method':'DELETE',
        'code':200,
        'message':'DELETE - You are authenticated',
        'result': {
            'email':'mail@email.com',
            'name':'John Doe',
            'roles':['staff', 'reporter']
        }
    })
