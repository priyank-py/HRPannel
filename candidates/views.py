from django.shortcuts import render, get_object_or_404
from .models import Candidate, HRRemark
from clients.models import Client, JobDetail
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Prefetch
import itertools

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


    #type="text"
    designation = request.GET.get('designation')
    if designation:
        candidates = candidates.filter(designation=designation)
    print(candidates)
    search_type = request.GET.get('search_type')
    any_keywords = request.GET.get('anykeywords')
    if any_keywords:
        any_keywords = {i.strip() for i in any_keywords.split(',')}
    all_keywords = request.GET.get('allkeywords')
    if all_keywords:
        all_keywords = {i.strip() for i in all_keywords.split(',')}
    exclude_keywords = request.GET.get('excludekeywords')
    if exclude_keywords:
        exclude_keywords = {i.strip() for i in exclude_keywords.split(',')}

    #type=radio
    search_in = request.GET.get('search_in')

    #type=checkbox
    include_without_resume = request.GET.get('include_without')
    exclude_without_resume = request.GET.get('exclude_without')
    if exclude_without_resume:
        candidates = candidates.exclude(resume__isnull=True)

    #type=text
    current_location = request.GET.get('current_location')

    # type=radio
    location_gate = request.GET.get('location_gate')

    # type=text
    preferred_location = request.GET.get('preferred_location')

# filter location basis:
    if location_gate == 'and':
        candidates = candidates.filter(
            Q(location=current_location) &
            Q(preferred_location=preferred_location)
        )
    elif location_gate == 'or':
        candidates = candidates.filter(
            Q(location=current_location) |
            Q(preferred_location=preferred_location)
        )
    
    min_experience = request.GET.get('min_experience')
    max_experience = request.GET.get('max_experience')
    min_salary = request.GET.get('min_salary')
    max_salary = request.GET.get('max_salary')

# filter salary
    if min_salary:
        candidates = candidates.filter(expected_salary__gte=min_salary)
    if max_salary:
        candidates = candidates.filter(expected_salary__lte=max_salary)

    # type=checkbox
    include_zero_salary = request.GET.get('zerosalary')
    if include_zero_salary:
        candidates = candidates.filter(current_salary__gt=0)

    # type=text
    notice_period = request.GET.get('notice')
    if notice_period:
        candidates = candidates.filter(notice_period__lte=notice_period)

    #Employment_Details:
    current_industry = request.GET.get('current_industry')
    current_department = request.GET.get('current_department')

    if current_department:
        candidates = candidates.filter(experiences__job_profile=job_profile)

    min_age = request.GET.get('min_age')
    if min_age:
        if min_age.isdigit():
            min_age = int(min_age)
            candidates = candiates.filter(age__gte=min_age)

    max_age = request.GET.get('max_age')
    if max_age:
        if max_age.isdigit():
            max_age = int(max_age)
            candidates = candidates.filter(age__lte=max_age)

    team_size_managed = request.GET.get('teamsize')
    include_companies = request.GET.get('include_companies')
    exclude_companies = request.GET.get('exclude_companies')

    #Education_Details:
    degree = request.GET.get('degree')

    candidates_ids = []
    all_keys = []
    any_keys = []
    exclude_keys = []
    min_exp = []
    max_exp = []
    for candidate in candidates:

        total_exp = 0
        for exp in candidate.experiences.all():
            total_exp += exp.total_experience
        total_exp = total_exp//365.2425
        if min_experience:
            if total_exp > min_experience:
                min_exp.append(candidate.id)
        if max_experience:
            if total_exp < max_experience:
                max_exp.append(candidate.id)

        #Basic_info Final
        basic_info = [candidate.name, candidate.phone_number, candidate.alternate_number, candidate.location, candidate.preferred_location, candidate.designation]

        qualification = [i.qualification for i in candidate.educations.all()]
        degree = [i.qualification for i in candidate.educations.all()]
        college_name = [i.college_name for i in candidate.educations.all()]
        education_info = [i for i in zip(qualification, degree, college_name)]
        # Education final
        education_info = [i for tup in education_info for i in tup]

        company = [i.company for i in candidate.experiences.all()]
        job_profile = [i.job_profile for i in candidate.experiences.all()]
        experience_info = [i for i in zip(company, job_profile)]
        # Experience final
        experience_info = [i for tup in experience_info for i in tup]

        # Skill final
        skill_info = [i.name for i in candidate.skills.all()]

        remarks = [i.remark for i in candidate.remarks.all()]
        status = [i.status for i in candidate.remarks.all()]
        considered_for = [i.considered_for for i in candidate.remarks.all()]
        # Remarks final
        hr_remarks = [i for i in zip(remarks, status, considered_for)]
        hr_remarks = [i for tup in hr_remarks for i in tup]

        ##Basic info
        if search_in == 'full_profile':
            candidate_data = [basic_info, education_info, experience_info, skill_info, hr_remarks]
        candidate_data = [basic_info, education_info, experience_info, skill_info, hr_remarks]
        if search_in == 'profile_title_or_skill':
            candidate_data = [basic_info, skill_info]
        if search_in == 'keyskill':
            candidate_data = [skill_info]
        if search_in == 'profile_title':
            candidate_data = [basic_info]
        candidates_data = set(itertools.chain.from_iterable(candidate_data))

        if all_keywords:
            commons = all_keywords.intersection(candidates_data)
            if len(all_keywords) == len(commons):
                all_keys.append(candidate.id)
        
        if any_keywords:
            commonds = any_keywords.intersection(candidates_data)
            if any(commons):
                any_keys.append(candidate.id)
        
        if exclude_keywords:
            commons = exclude_keywords.intersection(candidates_data)
            if not any(commons):
                exclude_keys.append(candidate.id)
    
    if any(all_keys):
        candidates = candidates.filter(id__in=all_keys)
    
    if any(any_keys):
        candidates = candidates.filter(id__in=any_keys)
    
    if any(exclude_keys):
        candidates = candidates.exclude(id__in=exclude_keys)

    if any(min_exp):
        candidates = candidates.filter(id__in=min_exp)
    
    if any(max_exp):
        candidates = candidates.filter(id__in=max_exp)

    print(candidates)
    
    context = {
        'candidates': candidates
    }

    return render(request, 'candidates/all.html', context)




