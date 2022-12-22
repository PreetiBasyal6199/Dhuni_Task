from rest_framework import serializers
from .models import *


class CandidateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields='__all__'


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('title',)