from rest_framework import viewsets

from cards.models import Card
from cards.serializers.card import CardSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.order_by('streak', 'created_at')
    serializer_class = CardSerializer

