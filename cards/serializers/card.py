from cards.models import Card
from rest_framework import serializers


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'front', 'back', 'streak', 'created_at']

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)