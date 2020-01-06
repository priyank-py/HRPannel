from django.shortcuts import render, get_object_or_404
from .models import Candidate, HRRemark
from clients.models import Client, JobDetail
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Prefetch

# class GreetingView(View):
#     greeting = "Good Day"

#     def get(self, request):
#         return HttpResponse(self.greeting)

# class MorningGreetingView(GreetingView):
#     greeting = "Morning to ya"


def all_candidates(request):
    candidate_list = Candidate.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(candidate_list, 20)
    try:
        candidates = paginator.page(page)
    except PageNotAnInteger:
        candidates = paginator.page(1)
    except EmptyPage:
        candidates = paginator.page(paginator.num_pages)

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
    education_background = request.GET.get('education')
    candidates = Candidate.objects.all().filter(
        (Q(name__icontains=query) | 
        Q(phone_number__icontains=query)) &
        Q(educations__qualification__icontains=education_background)
    )
    context = {
        'candidates': candidates,
    }
    return render(request, 'candidates/filtered.html', context)
        # return super().get_queryset()
    

def each_candidate(request, pk):
    candidate = get_object_or_404(Candidate, id=pk)
    context = {
        'candidate': candidate,
    }
    return render(request, 'candidates/each_candidate.html', context)


def short_listed_candidates(request):
    queryset = HRRemark.objects.only('considered_for')
    candidates = Candidate.objects.prefetch_related(Prefetch('remarks', queryset=queryset))
    print(queryset)
    context = {
        'candidates':candidates
    }
    return render(request, 'candidates/all.html', context)

def advance_search(request):
    return render(request, 'candidates/advanced_search.html')