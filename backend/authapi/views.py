from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from .authbackend import AuthBackend
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class AuthView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post (self, request) : 
        username = request.data['user']
        password = request.data['password']
        user = AuthBackend.authenticate(username=username)
        if (user):
            return JsonResponse(user)
        else:
            return JsonResponse({user: 'null'})

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return JsonResponse(content)