from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    # path('', {return HttpResponse("Working")),
    path('admin/', admin.site.urls),
    path('api/', include('articles.urls')),
    path('auth/',obtain_auth_token)
]
