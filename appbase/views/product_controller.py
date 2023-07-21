from django.http import JsonResponse

def all(request):
    return JsonResponse({
        'data':[
            {'name':'mazda', 'price':500000000},
            {'name':'toyota', 'price':700000000},
            {'name':'honda', 'price':800000000},
        ]
    })