from django.http import HttpResponse
from cardsGame.views.tools import JSONResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from cardsGame.models.player_model import Player
from cardsGame.models.bundle_model import Bundle
from cardsGame.models.user_model import User
from cardsGame.models.card_model import Card
from cardsGame.serializers.card_serializer import CardSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class CardList(APIView):
    def get(self, request, format=None):
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CardSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CardDetail(APIView):
    def get_object(self, acc_name):
        try:
            user = User.objects.filter(userName = acc_name)
            player = Player.objects.filter(user = user)
            bundles = Bundle.objects.filter(player = player)
            cards = Card.objects.filter(bundle = bundles)
            return cards
        except Card.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, acc_name, format = None):
        cards = self.get_object(acc_name)
        serializer = CardSerializer(cards, many=True)
        return JSONResponse(serializer.data)


    def put(self, request, acc_name, format = None):
        cards = self.get_object(acc_name)
        serializer = CardSerializer(cards, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, acc_name, format = None):
        cards = self.get_object(acc_name)
        cards.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

def cards_count(request, acc_name):

    try:
        player = Player.objects.get(acc_name=acc_name)
        bundle = Bundle.objects.filter(player = player)
        distribution = ''
        count = 0
        for i in range(0,len(bundle)):
            cards = Card.objects.filter(bundle = bundle[i]).count()
            count += cards
            distribution += str(cards) + ' in the bundle ' + bundle[i].name + '\n;   '


    except Card.DoesNotExist:
        return HttpResponse(status=404)

    message = acc_name + ' have ' +  str(count) + ' cards: \n' + distribution
    return HttpResponse(message)