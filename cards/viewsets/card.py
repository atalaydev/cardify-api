from http import HTTPStatus

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from cards.models import Card
from cards.serializers.card import CardSerializer

class CardViewSet(viewsets.ViewSet):
    queryset = Card.objects.all()
    serializers = CardSerializer

    def list(self, request):
        queryset = Card.objects.order_by('streak', 'created_at')[0]
        serializer = CardSerializer(queryset)

        return Response(
            serializer.data
        )

    def create(self, request):
        serializer = CardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(status=HTTPStatus.CREATED)

    def retrieve(self, request, pk=None):
        card = get_object_or_404(self.queryset, pk=pk)
        serializer = CardSerializer(card)

        return Response(
            serializer.data
        )

    @action(detail=True, methods=['GET'])
    def next(self, request, pk=None):
        queryset = Card.objects.exclude(id=pk).order_by('streak', 'created_at')[0]
        serializer = CardSerializer(queryset)

        return Response(
            serializer.data
        )

    @action(detail=True, methods=['PUT'])
    def streak(self, request, pk=None):
        if isinstance(request.data.get('value'), int):
            card = get_object_or_404(self.queryset, pk=pk)
            card.streak = request.data.get('value')
            card.save()
            return Response()
        
        return Response(status=HTTPStatus.BAD_REQUEST)
