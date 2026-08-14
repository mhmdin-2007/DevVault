from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import UserSerializer
from django.contrib.auth.models import User

class UserViewset(viewsets.ModelViewSet):
    """API endpoint for users."""
    
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]