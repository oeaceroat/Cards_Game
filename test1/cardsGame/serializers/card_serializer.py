from rest_framework import serializers
from cardsGame.models import Card,  LANGUAGE_CHOICES, STYLE_CHOICES


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('player', 'image', 'name', 'power')

    def create(self, validated_data):

        return Card.objects.create(**validated_data)

    def update(self, instance, validate_data):

        instance.player = validate_data.get('player', instance.player)
        instance.image = validate_data.get('image', instance.image)
        instance.name = validate_data.get('name', instance.name)
        instance.power = validate_data.get('power', instance.power)
        instance.save()
        return instance