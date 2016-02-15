from rest_framework import serializers
from cardsGame.models.card_model import Card,  LANGUAGE_CHOICES, STYLE_CHOICES
from cardsGame.serializers.concret_serializer import ConcretSerializer


class CardSerializer(ConcretSerializer):
    class Meta:
        model = Card
        fields = ('id', 'bundle', 'image', 'name', 'power')

    def create(self, validated_data):
        return Card.objects.create(**validated_data)

    def update(self, instance, validate_data):

        instance.bundle = validate_data.get('bundle', instance.bundle)
        instance.image = validate_data.get('image', instance.image)
        instance.name = validate_data.get('name', instance.name)
        instance.power = validate_data.get('power', instance.power)
        instance.save()
        return instance