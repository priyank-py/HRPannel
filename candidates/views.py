from django.shortcuts import render
from .models import Candidate
from django.views import View
from django.http import HttpResponse

# class GreetingView(View):
#     greeting = "Good Day"

#     def get(self, request):
#         return HttpResponse(self.greeting)

# class MorningGreetingView(GreetingView):
#     greeting = "Morning to ya"


def all_candidates(request):
    return render(request, 'candidates/all.html')
