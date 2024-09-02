from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializer for name field"""

    name = serializers.CharField(max_length=10)