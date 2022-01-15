from django_filters import rest_framework as filters
from cards.models import Card


class CardFilterSet(filters.FilterSet):
    class Meta:
        model = Card
        fields = {
            'bucket': ['exact'],
        }
