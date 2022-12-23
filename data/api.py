from rest_framework import views, generics
from rest_framework.response import Response
from django.db.models import Count
from .models import *
from .serializers import (CandidateListCreateSerializer,JobListCreateSerialzier, SelectJobSerializer, JobSkillListSerialzier,
                    JobSkillCreateSerializer, CandidateSkillCreateSerializer, CandidateSkillListSerializer, MostMatchedCandidateListSerialzier)
from .mixins import DynamicSerializerClassMixin
from django.shortcuts import get_object_or_404



class JobListCreateView(generics.ListCreateAPIView):
    serializer_class = JobListCreateSerialzier
    queryset = Job.objects.all()


class JobSkillListCreateView(DynamicSerializerClassMixin, generics.ListCreateAPIView):
    serializer_class = JobSkillCreateSerializer
    queryset =JobSkill.objects.all()
    serializer_action_classes = {
        'GET': JobSkillListSerialzier
    }


class CandidateListCreateView(generics.ListCreateAPIView):
    serializer_class = CandidateListCreateSerializer
    queryset = Candidate.objects.all()


class CandidateSkillListCreateView(DynamicSerializerClassMixin, generics.ListCreateAPIView):
    serializer_class = CandidateSkillCreateSerializer
    queryset =CandidateSkill.objects.all()
    serializer_action_classes = {
        'GET': CandidateSkillListSerializer
    }



class MostMatchedCandidateListView(views.APIView):

    def post(self,request, *args, **kwargs):
        '''
        input argument: 'title'
        out_put arguments: 'first_name','last_name'
        '''
        serializer = SelectJobSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        job_title = serializer.validated_data["title"]
        job = get_object_or_404(Job, title=job_title.lower())
        job_skills = job.jobskill_set.all().values_list("skill", flat=True)
        candidates = Candidate.objects.filter(candidateskill__skill__in=job_skills).annotate(
            skills_matching_count=Count('candidateskill__skill')).order_by('-skills_matching_count')
        if candidates:
            return Response(MostMatchedCandidateListSerialzier(candidates, many=True).data)
        return Response({
            'error':'No Candidates found with matching job skills.', 
        }, status= 404)
        
