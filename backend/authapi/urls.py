from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import AuthView

urlpatterns = [
    path('token_auth/', AuthView.as_view(), name="token_auth"),
    path('login/', obtain_auth_token, name='login'), 
]