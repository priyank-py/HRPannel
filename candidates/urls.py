from django.urls import path
from . import views

urlpatterns = [
    path('all', views.all_candidates, name="all_candidates"),
]
