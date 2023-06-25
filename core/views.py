from django.shortcuts import render
from django.http import JsonResponse


# third party imports
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
        'name' : 'james',
        'city' : 'nairobi',
        'address' : 123
        }
        return Response(data)


  
# def test_view(request):
#     data = {
#         'name' : 'james',
#         'city' : 'nairobi',
#         'address' : 123
#     }

#     return JsonResponse(data)