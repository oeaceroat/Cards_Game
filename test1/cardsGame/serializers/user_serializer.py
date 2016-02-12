from rest_framework import serializers
from cardsGame.models.user_model import User,  LANGUAGE_CHOICES, STYLE_CHOICES


class UserSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(UserSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = User
        fields = ('id', 'name', 'userName')

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

