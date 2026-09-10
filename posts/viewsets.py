from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    '''
    Allow read access to everyone, but only the owner of an object can modify or delete it.
    '''

    def has_object_permission(self, request, view, obj):
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True

        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)