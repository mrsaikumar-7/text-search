# authentication/serializers.py
from rest_framework import serializers
from .models import CustomUser

# Serializer for CustomUser model
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # Define fields to include in the serialized output
        fields = ('id', 'name', 'email', 'dob', 'createdAt', 'modifiedAt', 'password')
        # Specify extra kwargs, marking 'password' field as write-only
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create a new CustomUser instance using the create_user method
        user = CustomUser.objects.create_user(**validated_data)
        return user

# Serializer for user login
class LoginSerializer(serializers.Serializer):
    # Fields for user login
    email = serializers.EmailField()
    password = serializers.CharField()
