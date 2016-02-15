from rest_framework import serializers
from cardsGame.models.concret_model import Concret,  LANGUAGE_CHOICES, STYLE_CHOICES

class ConcretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concret
        fields = ('bundle')

    def create(self, validated_data):
        return Concret.objects.create(**validated_data)

    def update(self, instance, validate_data):

        instance.bundle = validate_data.get('bundle', instance.bundle)
        instance.save()
        return instance

