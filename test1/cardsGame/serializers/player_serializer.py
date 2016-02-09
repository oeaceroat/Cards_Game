from rest_framework import serializers
from cardsGame.models import Player, LANGUAGE_CHOICES, STYLE_CHOICES

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('user', 'acc_name')

    def create(self, validated_data):
        """
        Create and return a new `Player` instance, given the validated data.
        """
        return Player.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `PLayer` instance, given the validated data.
        """
        instance.user = validated_data.get('user', instance.user)
        instance.acc_name = validated_data.get('acc_name', instance.acc_name)
        instance.save()
        return instance