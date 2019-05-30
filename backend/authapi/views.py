from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from .authbackend import AuthBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


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
        user = request.user
        first_name = user.first_name
        last_name = user.last_name
        content = {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'location': user.profile.location,
            'past_lessons': user.profile.past_lessons,
            'upcoming_lessons': user.profile.upcoming_lessons,
            'protocol_url': user.profile.protocol_url,
            'folder_url': user.profile.folder_url
        }
        return JsonResponse(content)

    def update_profile(request, user_id):
        user = User.objects.get(pk=user_id)
        user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
        user.save()

