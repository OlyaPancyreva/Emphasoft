from rest_framework import viewsets
from .serializers import *


class UserView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
