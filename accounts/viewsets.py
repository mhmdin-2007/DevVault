from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

class UserViewset(viewsets.ReadOnlyModelViewSet):
    """API endpoint for users."""
    
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]