from django.urls import path
from . import views

urlpatterns = [
    path('', views.all, name="all_clients"),
    path('add', views.add, name="add_clients"),
    path('all_jobs', views.all_jobs, name="all_jobs"),
]
