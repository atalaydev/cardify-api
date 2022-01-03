from rest_framework import viewsets

from cards.models import Card
from cards.serializers.card import CardSerializer

class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer

    def get_queryset(self):
        return Card.objects.order_by('streak', 'created_at')
