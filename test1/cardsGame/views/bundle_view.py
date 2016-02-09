from django.http import HttpResponse
from cardsGame.views.tools import JSONResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from cardsGame.models.player_model import Player
from cardsGame.models.bundle_model import Bundle

from cardsGame.serializers.bundle_serializer import BundleSerializer


@csrf_exempt
def bundle_list(request):

    if request.method == 'GET':
        bundles = Bundle.objects.all()
        serializer = BundleSerializer(bundles, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BundleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def bundle_detail(request, acc_name):
    try:
        player = Player.objects.filter(acc_name=acc_name)
        bundle = Bundle.objects.filter(player = player)

    except Bundle.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BundleSerializer(bundle, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BundleSerializer(bundle, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status = 400)

    elif request.method == 'DELETE':
        bundle.delete()
        return HttpResponse(status=204)