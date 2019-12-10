from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm

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