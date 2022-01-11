from rest_framework import viewsets

from cards.models import Card
from cards.serializers.card import CardSerializer

class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer

    def get_queryset(self):
        return Card.objects \
            .filter(created_by=self.request.user) \
            .order_by('streak', 'created_at')

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
