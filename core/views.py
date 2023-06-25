from django.shortcuts import render
from django.http import JsonResponse


# third party imports
from rest_framework.response import Response
from rest_framework.views import APIView

from . serializers import PostSerializer, GetSerializer
from . models import Post

# Create your views here.
class TestView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        post = qs.first()
        # serializer = PostSerializer(qs, many=True)
        serializer = GetSerializer(post)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


  
# def test_view(request):
#     data = {
#         'name' : 'james',
#         'city' : 'nairobi',
#         'address' : 123
#     }

#     return JsonResponse(data)