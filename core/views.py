from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def test_view(request):
    data = {
        'name' : 'james',
        'city' : 'nairobi',
        'address' : 123
    }

    return JsonResponse(data)