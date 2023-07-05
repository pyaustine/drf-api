from django.contrib import admin
from django.urls import path, include
from core.views import TestView

# third party imports
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api-auth/', include('rest_framework.urls')),
    path('', TestView.as_view(), name='test'),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    # path('rest-auth/', include('rest_auth.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
