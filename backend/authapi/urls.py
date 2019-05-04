from django.urls import path
from .views import AuthView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('token_auth/', AuthView.as_view(), name="token_auth"),
    path('login/', obtain_auth_token, name='login'), 
]