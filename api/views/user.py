from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet

from api.models import User


# Serializers
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class UserSerializerLogin(UserSerializer):
    token = serializers.SerializerMethodField()

    @staticmethod
    def get_token(user):
        token, created = Token.objects.get_or_create(user=user)
        return token.key

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'token')


# Viewsets
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
