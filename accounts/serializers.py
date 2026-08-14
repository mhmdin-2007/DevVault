from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    """ Serializer for Profile model. """

    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'github_url', 'linkedin_url']

class UserSerializer(serializers.ModelSerializer):
    """ Serializer for User model."""

    profile = ProfileSerializer(read_only=True) 

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile']
        read_only_fields = ['id']