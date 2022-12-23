from django.urls import path
from .api import (MostMatchedCandidateListView, JobListCreateView, JobSkillListCreateView, CandidateListCreateView, CandidateSkillListCreateView)


urlpatterns = [
    path('job/',JobListCreateView.as_view(), name='job_list_create_view'),
    path('job-skill/',JobSkillListCreateView.as_view(), name='job_skill_list_create'),
    path('candidate/',CandidateListCreateView.as_view(), name='candidate_list_create'),
    path('candidate-skill/',CandidateSkillListCreateView.as_view(), name='candidate_skill_list_create'),
    path('candidates/most-matched/',MostMatchedCandidateListView.as_view(), name='most_matched_candidateview'),
]
