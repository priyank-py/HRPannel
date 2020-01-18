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


def advance_result(request):
    candidates = Candidate.objects.all()
    # candidates_set = {c.id:{c.name, c.location, c.designation, {{e.qualification, e.degree,e.college_name} for e in c.educations.all()}, {{e.company, e.job_profile} for e in c.experiences.all()}, {s.name for s in c.skills.all()}, {{r.status, r.considered_for for r in c.remarks.all()]} for c in candidates}
    # print(candidates_set)

    for candidate in candidates:
        pass



    #type="text"
    designation = request.GET.get('designation')
    if designation:
        candidates = candidates.filter(designation=designation)
    print(candidates)
    search_type = request.GET.get('search_type')
    any_keywords = request.GET.get('anykeywords')
    any_keywords = [i.strip() for i in any_keywords.split(',')]
    all_keywords = request.GET.get('allkeywords')
    all_keywords = [i.strip() for i in any_keywords.split(',')]
    exclude_keywords = request.GET.get('excludekeywords')

    #type=radio
    search_in = request.GET.get('search_in')

    if search_in == 'full_profile':
        candidates = candidates.filter(
            Q(name__in=any_keywords)
        )

    #type=checkbox
    include_without_resume = request.GET.get('include_without')
    exclude_without_resume = request.GET.get('exclude_without')

    #type=text
    current_location = request.GET.get('current_location')

    # type=radio
    location_gate = request.GET.get('location_gate')

    # type=text
    preferred_location = request.GET.get('preferred_location')
    
    min_experience = request.GET.get('min_experience')
    max_experience = request.GET.get('max_experience')
    min_salary = request.GET.get('min_salary')
    max_salary = request.GET.get('max_salary')

    # type=checkbox
    include_zero_salary = request.GET.get('zerosalary')

    # type=text
    notice_period = request.GET.get('notice')

    #Employment_Details:
    current_industry = request.GET.get('current_industry')
    current_department = request.GET.get('current_department')
    min_age = request.GET.get('min_age')
    max_age = request.GET.get('max_age')
    team_size_managed = request.GET.get('teamsize')
    include_companies = request.GET.get('include_companies')
    exclude_companies = request.GET.get('exclude_companies')

    #Education_Details:
    degree = request.GET.get('degree')
    return render(request, 'candidates/advanced_search.html')




