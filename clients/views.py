from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from clients.models import Client, JobDetail

# Create your views here.
def all(request):
    pass

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

def all_jobs(request):
    client_list = Client.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(client_list, 20)
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

def filtered_jobs(request):
    q = request.GET.get('q')
    client_list = Client.objects.all().filter(name=q)
    page = request.GET.get('page', 1)
    paginator = Paginator(client_list, 20)
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
   

   