from rest_framework import viewsets

from .models import Users
from .serializers import *


class UserView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
