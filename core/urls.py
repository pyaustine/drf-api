from django.urls import path, include
from views import TestView

# third party imports
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', TestView.as_view(), name='test'),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
