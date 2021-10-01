from rest_framework import viewsets, permissions

from .models import Users
from .serializers import *


class UserView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Users.objects.all()
    serializer_class = UserSerializer

