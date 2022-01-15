from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from cards.models import Card
from cards.serializers import CardSerializer
from cards.filtersets import CardFilterSet


class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CardFilterSet

    def get_queryset(self):
        return Card.objects \
            .filter(created_by=self.request.user) \
            .order_by('streak', 'created_at')

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
