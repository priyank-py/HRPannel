from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('all', views.all_candidates, name="all_candidates"),
    # path('bout/', TemplateView.as_view(template_name="about.html")),
    # path('about/', vGreetingView.as_view(greeting="G'day")),
]
