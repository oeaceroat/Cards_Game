from django.http import HttpResponse
from cardsGame.views.tools import JSONResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from cardsGame.models.user_model import User
from cardsGame.models.player_model import Player
from cardsGame.serializers.player_serializer import  PlayerSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import HttpResponse, Http404


class PlayerList(APIView):
    """
    List all code cardsGame, or create a new user.
    """
    def get(self, request, format=None):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = PlayerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlayerDetail(APIView):
    """
    Retrieve, update or delete a code user.
    """
    def get_object(self, userName):
        try:
            user_ = User.objects.filter(userName = userName)
            player = Player.objects.filter(user = user_)

        except Player.DoesNotExist:
            raise Http404

    def get(self, request, userName, format=None):
        players = self.get_object(userName)
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    def put(self, request, userName, format=None):
        player = self.get_object(userName)
        serializer = PlayerSerializer(player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUES)

    def delete(self, request, userName, format=None):
        player = self.get_object(userName)
        player.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

