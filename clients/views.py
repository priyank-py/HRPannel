from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from clients.models import Client, JobDetail
from django.db.models import Q


# def all(request):
#     pass

def add(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid:
            # post = form.save(commit=False)
            # post.save()
            form.save()
        return redirect('/')
    else:
        form = ClientForm()
    return render(request, 'clients/add.html', {'form': form})

def all(request):
    client_list = Client.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(client_list, 10)
    try:
        clients = paginator.page(page)
    except PageNotAnInteger:
        clients = paginator.page(1)
    except EmptyPage:
        clients = paginator.page(paginator.num_pages)

    context = {
        'clients': clients,
    }

    return render(request, 'clients/all.html', context)

def filtered_clients(request):
    q = request.GET.get('q')
    company_type = request.GET.get('education')
    client_list = Client.objects.all().filter(
        Q(name__icontains=q) & 
        Q(company_type__iexact=company_type ))
    page = request.GET.get('page', 1)
    paginator = Paginator(client_list, 10)
    try:
        clients = paginator.page(page)
    except PageNotAnInteger:
        clients = paginator.page(1)
    except EmptyPage:
        clients = paginator.page(paginator.num_pages)

    context = {
        'clients': clients,
    }

    return render(request, 'clients/all.html', context)


def each_client(request, id):
    client = get_object_or_404(Client, id=id)
    
    context = {
        'client': client,
    }
    return render(request, 'clients/each_client.html', context)



def all_jobs(request):
    job_list = JobDetail.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(job_list, 10)
    try:
        jobs = paginator.page(page)
    except PageNotInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)
    context = {
        'jobs': jobs,
    }
    return render(request, 'clients/all_jobs.html', context)

def filtered_jobs(request):
    q = request.GET.get('q')
    job_list = JobDetail.objects.all().filter(designation__icontains=q)
    page = request.GET.get('page', 1)
    paginator = Paginator(job_list, 10)
    try:
        jobs = paginator.page(page)
    except PageNotInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)
    context = {
        'jobs': jobs,
    }
    return render(request, 'clients/all_jobs.html', context)

def job(request, id):
    job = get_object_or_404(JobDetail, id=id)
    # print(job.required_skills.names())
    context = {
        'job': job,
    }
    return render(request, 'clients/each_job.html', context)

