from app.models import Users
from django.contrib.auth.models import User
from rest_framework import serializers


class ReadOnly(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'is_active',
                  'last_login', 'is_superuser',)


# read only
class UserSerializerReadOnly(serializers.ModelSerializer):
    user = ReadOnly(read_only=True)

    class Meta:
        model = Users
        fields = ('user',)


class UserSerializerWriteOnly(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'