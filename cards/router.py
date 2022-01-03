from cards.viewsets.card import CardViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'cards', CardViewSet)
