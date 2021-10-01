from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

User = get_user_model()


class UserSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'is_active',
                  'last_login', 'is_superuser', 'password')
