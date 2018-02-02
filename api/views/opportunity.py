from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from api.models import Opportunity


# Serializers
class OpportunitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Opportunity
        fields = '__all__'


# Viewsets
class OpportunityViewSet(ModelViewSet):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
