from django.urls import path
from . import views
# from.views import SearchResultsListView
# from django.views.generic import TemplateView

urlpatterns = [
    path('all', views.all_candidates, name="all_candidates"),
    path('filtered', views.filtered_candidates, name="filtered_candidates")
    # path('bout/', TemplateView.as_view(template_name="about.html")),
    # path('about/', vGreetingView.as_view(greeting="G'day")),
    # path('search/', SearchResultsListView.as_view(), name='search_results'),
]

