from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from chatting.serializers import *
from chatting.models import *
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.http import HttpResponse

class BoxListCreate(generics.ListCreateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

class BoxEnter(generics.CreateAPIView):
    serializer_class = BoxEnterSerializer

    def post(self, request, format='json'):
        user = User.objects.get(int(request.POST['user_id']))
        box = Box.objects.get(int(request.POST['box_id']))

        user.box.add(box)


class BoxExit(generics.CreateAPIView):
    serializer_class = BoxEnterSerializer

    def post(self, request, format='json'):
        user = User.objects.get(int(request.POST['user_id']))
        box = Box.objects.get(int(request.POST['box_id']))
        user.box.remove(box)

class UserListCreate(generics.ListCreateAPIView):
    """
    Creates the user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


    # def post(self, request, format='json'):
    #     serializers = UserSerializer(data=request.data)
    #     if serializers.is_valid():
    #         user = serializers.save()
    #         if user:
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response('hello')
