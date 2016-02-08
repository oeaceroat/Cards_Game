from rest_framework import serializers
from cardsGame.models import User, Player, Card,  LANGUAGE_CHOICES, STYLE_CHOICES


class UserSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(UserSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = User
        fields = ('name', 'userName')

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.userName = validated_data.get('userName', instance.userName)
        instance.save()
        return instance
        """
        Update and return an existing `User` instance, given the validated data.
        """


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


