from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    ''' Serializer for Post model. converts Post instance to JSON and vice versa.'''

    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'author_username', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']
