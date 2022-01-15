from cards.models import Card
from rest_framework import serializers


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ['key', 'bucket', 'front', 'back', 'confidence', 'streak', 'created_at']
        read_only_fields = ['created_at']
