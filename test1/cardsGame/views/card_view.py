from django.http import HttpResponse
from cardsGame.views.tools import JSONResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from cardsGame.models import User, Player, Card
from cardsGame.serializers.card_serializer import CardSerializer


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