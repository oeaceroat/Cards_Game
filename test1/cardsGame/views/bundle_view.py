from django.http import HttpResponse, Http404
from cardsGame.views.tools import JSONResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from cardsGame.models.player_model import Player
from cardsGame.models.bundle_model import Bundle
from cardsGame.models.concret_model import Concret
from cardsGame.serializers.bundle_serializer import BundleSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class BundleList(APIView):
    def get(self, request, format=None):
        bundles = Bundle.objects.all()
        serializer = BundleSerializer(bundles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BundleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BundleDetail(APIView):
    def get_object(self, acc_name):
        try:
            player = Player.objects.filter(acc_name=acc_name)
            bundles = Bundle.objects.filter(player = player)
            return bundles
        except Bundle.DoesNotExist:
            raise Http404

    def get(self, request, acc_name, format=None):
        bundles = self.get_object(acc_name)
        serializer = BundleSerializer(bundles, many=True)
        return Response(serializer.data)

    def put(self, request, acc_name, format=None):
        bundle = self.get_object(acc_name)
        serializer = BundleSerializer(bundle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, acc_name, format=None):
        bundle = self.get_object(acc_name)
        bundle.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


def bundle_merge(request, bundle_source_id, bundle_destination_id ):

    try:
        bundle_source = Bundle.objects.get(id = bundle_source_id)
        bundle_destination = Bundle.objects.get(id = bundle_destination_id)
    except Bundle.DoesNotExist:
        return  HttpResponse(status = 404)


    concret_source = Concret.objects.filter(bundle= bundle_source)

    for i in range(0, len(concret_source)):
        concret = concret_source[i]
        concret.bundle = bundle_destination
        concret.save()

    bundle_source.delete()

    messagge = 'Merge ok'
    return HttpResponse(messagge)


def bundle_exchange(request, bundle_player1_id, bundle_player2_id):
    try:
        bundle_player1 = Bundle.objects.get(id = bundle_player1_id)
        bundle_player2 = Bundle.objects.get(id = bundle_player2_id)
    except Bundle.DoesNotExist:
        return HttpResponse(status=404)

    aux =  bundle_player1.player
    bundle_player1.player = bundle_player2.player
    bundle_player1.save()
    bundle_player2.player = aux
    bundle_player2.save()

    messagge = 'Exchange ok'
    return HttpResponse(messagge)


class BundleDivide(APIView):

    def post(self, request, format=None):
        concret_id_list = request.data.get('concret_id')
        player_destination_id = request.data.get('player_destination_id')
        print type(player_destination_id)
        try:
            #bundle_source = Bundle.objects.get(id=bundle_source_id)
            player_destination = Player.objects.get(player_destination_id)
        except Player.DoesNotExist:
            return HttpResponse(status=404)

        new_bundle = Bundle(player=player_destination_id, name="new bundle",type=2)
        new_bundle.save()

        for i in range(0, len(concret_id_list)):
            concret = Concret.objects.get(id=concret_id_list[i])
            concret.bundle = new_bundle
            concret.save()

        messagge = 'Divide ok'
        return HttpResponse(messagge)













