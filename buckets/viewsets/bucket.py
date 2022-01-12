from rest_framework import viewsets

from buckets.models import Bucket
from buckets.serializers.bucket import BucketSerializer

class BucketViewSet(viewsets.ModelViewSet):
    serializer_class = BucketSerializer

    def get_queryset(self):
        return Bucket.objects \
            .filter(created_by=self.request.user) \
            .order_by('created_at')

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
