from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from cardsGame.models import User, Player, Card
from cardsGame.serializers import UserSerializer, PlayerSerializer, CardSerializer
from rest_framework import serializers

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


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

@csrf_exempt
def player_list(request):
    """
    List all code cardsGame, or create a new user.
    """
    if request.method == 'GET':
        cardsGame = Player.objects.all()
        serializer = PlayerSerializer(cardsGame, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PlayerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def player_detail(request, userName):
    """
    Retrieve, update or delete a code user.
    """
    try:
        user_ = User.objects.filter(userName = userName)
        player = Player.objects.filter(user = user_)

    except Player.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PlayerSerializer(player, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PlayerSerializer(player, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        player.delete()
        return HttpResponse(status=204)

@csrf_exempt
def card_list(request):

    if request.method == 'GET':
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CardSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def card_detail(request, userName):
    try:
        user = User.objects.filter(userName = userName)
        player = Player.objects.filter(user = user)
        card = Card.objects.filter(player = player)

    except Card.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CardSerializer(card, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CardSerializer(card, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status = 400)

    elif request.method == 'DELETE':
        card.delete()
        return HttpResponse(status=204)

def cards_count(request, acc_name):

    try:
        player = Player.objects.get(acc_name=acc_name)
        count = Card.objects.filter(player = player).count()

    except Player.DoesNotExist:
        return HttpResponse(status=404)

    message = (acc_name, ' have ', count, ' cards ')
    return HttpResponse(message)



