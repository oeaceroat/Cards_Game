from django.http import HttpResponse
from cardsGame.views.tools import JSONResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from cardsGame.models.user_model import User
from cardsGame.models.player_model import Player
from cardsGame.serializers.player_serializer import  PlayerSerializer


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