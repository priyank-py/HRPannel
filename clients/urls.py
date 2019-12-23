from django.urls import path
from . import views

urlpatterns = [
    path('', views.all, name="all_clients"),
    path('add', views.add, name="add_clients"),
    path('all_jobs', views.all_jobs, name="all_jobs"),
    path('filtered_jobs', views.filtered_jobs, name="filtered_jobs"),
    path('filtered_clients', views.filtered_clients, name="filtered_clients"),
    path('<int:id>/job', views.job, name="each_job"),
]
