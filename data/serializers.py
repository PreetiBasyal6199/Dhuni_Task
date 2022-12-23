from rest_framework import serializers
from .models import *


class CandidateListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields='__all__'


class SelectJobSerializer(serializers.Serializer):
    title = serializers.CharField()


class JobListCreateSerialzier(serializers.ModelSerializer):
    class Meta:
        model =Job
        fields = ("title", )


class JobSkillCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSkill
        fields = '__all__'
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=JobSkill.objects.all(),
                fields=("job", "skill"),
                message="The skill with this job is already created.Please add another skill."

            )
        ]


class JobSkillListSerialzier(serializers.ModelSerializer):
    job = serializers.CharField(source="job.title")
    class Meta:
        model = JobSkill
        fields ='__all__'


class CandidateSkillListSerializer(serializers.ModelSerializer):
    candidate = serializers.CharField(source="candidate.get_full_name")
    class Meta:
        model =CandidateSkill
        fields = "__all__"


class CandidateSkillCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateSkill
        fields ="__all__"
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=CandidateSkill.objects.all(),
                fields=("candidate", "skill"),
                message="You have already added this skill.Please add another one."

            )
        ]


class MostMatchedCandidateListSerialzier(serializers.ModelSerializer):
    skills_matching_count = serializers.IntegerField()

    class Meta:
        model = Candidate
        fields = "__all__"
