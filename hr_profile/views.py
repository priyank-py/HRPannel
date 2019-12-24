from django.shortcuts import render
from clients.models import JobDetail, Client
from candidates.models import Candidate
from datetime import date, datetime
# Create your views here.
def dashboard(request):
    today = date.today()
    all_active_jobs = JobDetail.objects.filter(agreement__start_date__lte=today).filter(agreement__start_date__gte=today)
    active_job_num = len(all_active_jobs)
    print(active_job_num)

    all_clients_count = Client.objects.all().count()

    all_candidates_count = Candidate.objects.all().count()
    context = {
        'active_job_num': active_job_num,
        'all_clients_count': all_clients_count,
        'all_candidates_count': all_candidates_count,
    }
    return render(request, 'main/home.html', context)