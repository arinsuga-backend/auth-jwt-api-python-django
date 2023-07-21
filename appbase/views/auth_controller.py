from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def authenticate(request):
    #GET Request
    if request.method == 'GET':
        return get_auth(request=request)

    #POST Request
    if request.method == 'POST':
        return post_auth(request=request)

    #PUT Request
    if request.method == 'PUT':
        return put_auth(request=request)

    #PATCH Request
    if request.method == 'PATCH':
        return patch_auth(request=request)
    
    #DELETE Request
    if request.method == 'DELETE':
        return delete_auth(request=request)

#GET method
def get_auth(request):
    return JsonResponse({
        'method':'GET',
        'code':200,
        'message':'GET - You are authenticated',
        'result': {
            'email':'mail@email.com',
            'name':'John Doe',
            'roles':['staff', 'reporter']
        }
    })

#POST method
def post_auth(request):
    return JsonResponse({
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

#PUT method
def put_auth(request):
    return JsonResponse({
        'method':'PUT',
        'code':200,
        'message':'PUT - You are authenticated',
        'result': {
            'email':'mail@email.com',
            'name':'John Doe',
            'roles':['staff', 'reporter']
        }
    })

#PATCH method
def patch_auth(request):
    return JsonResponse({
        'method':'PATCH',
        'code':200,
        'message':'PATCH - You are authenticated',
        'result': {
            'email':'mail@email.com',
            'name':'John Doe',
            'roles':['staff', 'reporter']
        }
    })

#DELETE method
def delete_auth(request):
    return JsonResponse({
        'method':'DELETE',
        'code':200,
        'message':'DELETE - You are authenticated',
        'result': {
            'email':'mail@email.com',
            'name':'John Doe',
            'roles':['staff', 'reporter']
        }
    })
