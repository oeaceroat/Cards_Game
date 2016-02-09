from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from cardsGame.views.tools import JSONResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from cardsGame.models.user_model import User
from cardsGame.serializers.user_serializer import UserSerializer
from rest_framework import serializers

@csrf_exempt
def user_list(request):
    """
    List all code cardsGame, or create a new user.
    """
    if request.method == 'GET':
        cardsGame = User.objects.all()
        serializer = UserSerializer(cardsGame, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def user_detail(request, userName):
    """
    Retrieve, update or delete a code user.
    """
    try:
        user = User.objects.filter(userName=userName)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)