from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers.employee import EmployeeSerializer
from ..models.employee import Employee

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def employees(request):
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

# GET Action
def get_action(request):
    serializer=EmployeeSerializer(Employee)
    return Response({ 'data':serializer.data })

# POST Action
def post_action(request):
    return Response({ 'data':'POST - Employee' })

# PUT Action
def put_action(request):
    return Response({ 'data':'PUT - Employee' })

# PATCH Action
def patch_action(request):
    return Response({ 'data':'PATCH - Employee' })

# DELETE Action
def delete_action(request):
    return Response({ 'data':'DELETE - Employee' })
