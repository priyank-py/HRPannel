from django.shortcuts import render
from .models import Candidate


def all_candidates(request):
    return render(request, 'candidates/all.html')
