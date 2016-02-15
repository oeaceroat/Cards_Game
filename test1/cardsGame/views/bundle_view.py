from django.http import HttpResponse, Http404
from cardsGame.views.tools import JSONResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from cardsGame.models.player_model import Player
from cardsGame.models.bundle_model import Bundle
from cardsGame.models.concret_model import Concret
from cardsGame.models.bundle_type_model import BundleType
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


class BundleMerge(APIView):

    def post(self, request, format=None):
        bundle_source_id = request.data.get('bundle_source_id')
        bundle_destination_id = request.data.get('bundle_destination_id')
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


class BundleExchange(APIView):

    def post(self, request, format=None):
        bundle1_id = request.data.get('bundle1_id')
        bundle2_id = request.data.get('bundle2_id')

        try:
            bundle1 = Bundle.objects.get(id = bundle1_id)
            bundle2 = Bundle.objects.get(id = bundle2_id)
        except Bundle.DoesNotExist:
            return HttpResponse(status=404)

        aux =  bundle1.player
        bundle1.player = bundle2.player
        bundle1.save()
        bundle2.player = aux
        bundle2.save()

        messagge = 'Exchange ok'
        return HttpResponse(messagge)


class BundleDivide(APIView):

    def post(self, request, format=None):

        concret_id_list = request.data.get('concret_id_list')
        player_id = request.data.get('player_id')
        bundle_type_id = request.data.get('bundle_type_id')
        bundle_source_id = Concret.objects.get(id=concret_id_list[0]).bundle.id
        try:
            player = Player.objects.get(id = player_id)
        except Player.DoesNotExist:
            return HttpResponse(status=404)
        try:
            bundle_type = BundleType.objects.get(id=bundle_type_id)
        except BundleType.DoesNotExist:
            return  HttpResponse(status=404)

        new_bundle = Bundle(player=player, name="new bundle",type=bundle_type)
        new_bundle.save()


        for i in range(0, len(concret_id_list)):
            concret = Concret.objects.get(id=concret_id_list[i])
            concret.bundle = new_bundle
            concret.save()

        bundle_source_count = Concret.objects.filter(bundle=Bundle.objects.get(id=bundle_source_id)).count()
        if(bundle_source_count == 0):
            bundle_source = Bundle.objects.get(id=bundle_source_id)
            bundle_source.delete()

        messagge = 'Divide ok'
        return HttpResponse(messagge)













