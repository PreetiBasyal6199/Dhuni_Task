from rest_framework import serializers
from .models import *


class CandidateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields='__all__'


class JobSerializer(serializers.Serializer):
    title = serializers.CharField()
