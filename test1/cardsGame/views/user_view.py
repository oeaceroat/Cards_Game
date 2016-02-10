from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.parsers import JSONParser
from cardsGame.models.user_model import User
from cardsGame.serializers.user_serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class UserList(APIView):
    """
    List all code cardsGame, or create a new user.
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve, update or delete a code user.
    """
    def get_object(self, userName):
        try:
            user = User.objects.filter(userName=userName)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, userName, format=None):
        users = self.get_object(userName)
        serializer = UserSerializer(users)
        return Response(serializer.data)

    def put(self, request, userName, format=None):
        user = self.get_object(userName)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, userName, format=None):
        user = self.get_object(userName)
        user.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)