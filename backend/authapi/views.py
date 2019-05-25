from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from .authbackend import AuthBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


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
        first_name = request.user.first_name
        last_name = request.user.last_name
        content = {'message': 'Welcome user: ' + first_name + " " + last_name}
        return JsonResponse(content)

