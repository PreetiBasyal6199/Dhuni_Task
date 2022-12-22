from django.urls import path
from .api import MostMatchedCandidateListView


urlpatterns = [
    path('most-matched/',MostMatchedCandidateListView.as_view(), name='most_matched_candidateview'),
]
