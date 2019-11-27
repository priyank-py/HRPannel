from django.shortcuts import render
from .models import Candidate
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q

# class GreetingView(View):
#     greeting = "Good Day"

#     def get(self, request):
#         return HttpResponse(self.greeting)

# class MorningGreetingView(GreetingView):
#     greeting = "Morning to ya"


def all_candidates(request):
    candidates = Candidate.objects.all()

    context = {
        'candidates': candidates,
    }

    return render(request, 'candidates/all.html', context)


# class SearchResultsListView(ListView):
#     model = Candidate
#     template_name = "candidates/filtered.html"

    # def get_queryset(self):
def filtered_candidates(request):
    query = request.GET.get('q')
    candidates = Candidate.objects.all().filter(
        Q(name__icontains=query) | 
        Q(phone_number__icontains=query)
    )
    context = {
        'candidates': candidates,
    }
    return render(request, 'candidates/filtered.html', context)
        # return super().get_queryset()
    

    