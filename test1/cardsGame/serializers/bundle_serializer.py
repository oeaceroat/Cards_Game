from rest_framework import serializers
from cardsGame.models.bundle_model import Bundle,  LANGUAGE_CHOICES, STYLE_CHOICES

class BundleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bundle
        fields = ('id','player', 'name')

    def create(self, validate_data):
        return Bundle.objects.create(**validate_data)

    def update(self, instance, validate_data):

        instance.player = validate_data.get('player'),
        instance.name = validate_data.get('name')
        instance.save()
        return instance