from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from api.models import NPO


# Serializers
class NPOSerializer(serializers.ModelSerializer):

    class Meta:
        model = NPO
        fields = '__all__'


# Viewsets
class NPOViewSet(ModelViewSet):
    queryset = NPO.objects.all()
    serializer_class = NPOSerializer
