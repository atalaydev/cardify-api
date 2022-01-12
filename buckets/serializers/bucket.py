from buckets.models import Bucket
from rest_framework import serializers


class BucketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bucket
        fields = ['id', 'name', 'status', 'created_at']
        read_only_fields = ['created_at']
