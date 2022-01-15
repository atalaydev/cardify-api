from buckets.viewsets import BucketViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'buckets', BucketViewSet, basename='bucket')
