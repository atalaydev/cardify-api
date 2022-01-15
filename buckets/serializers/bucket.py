from buckets.models import Bucket
from rest_framework import serializers


class BucketSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Bucket
        fields = ['url', 'name', 'status', 'created_at']
        read_only_fields = ['created_at']
