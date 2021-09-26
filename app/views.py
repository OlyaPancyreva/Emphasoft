from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from .serializers import *


class UserView(APIView):

    @staticmethod
    def post(request):
        user = UserSerializerWriteOnly(data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request):
        user_id = request.GET.get("id")
        users_list = Users.objects.all()
        if user_id:
            users_list = Users.objects.filter(user_id=user_id)
        serializer = UserSerializerReadOnly(users_list, many=True)
        return Response(serializer.data)


# get, update, patch, delete
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializerReadOnly
    queryset = Users.objects.all()
