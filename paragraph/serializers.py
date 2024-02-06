# paragraph/serializers.py
from rest_framework import serializers
from .models import Paragraph

# Serializer for the Paragraph model
class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        # Specify the model to be serialized
        model = Paragraph

        # Specify the fields to include in the serialized output
        fields = ['id', 'content']
