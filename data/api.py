from rest_framework import views
from rest_framework.response import Response
from django.db.models import Count
from .models import *
from .serializers import CandidateListSerializer, JobSerializer
from django.shortcuts import get_object_or_404

class MostMatchedCandidateListView(views.APIView):
    
    def post(self,request, *args, **kwargs):
        serializer = JobSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        job_title = serializer.validated_data["title"]
        job = get_object_or_404(Job, title=job_title)
        job_skills = job.jobskill_set.all().values_list("skill", flat=True)
        candidates = Candidate.objects.filter(candidateskill__skill__in=job_skills).annotate(
            skills_matching_count=Count('candidateskill__skill')).order_by('-skills_matching_count')
        if candidates:
            return Response(CandidateListSerializer(candidates, many=True).data)
        return Response({
            'error':'No matching Candidates found', 
        }, status= 404)
        
