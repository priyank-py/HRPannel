from django.urls import path
from . import views
# from.views import SearchResultsListView
# from django.views.generic import TemplateView

urlpatterns = [
    path('', views.all_candidates, name="all_candidates"),
    path('filtered', views.filtered_candidates, name="filtered_candidates"),
    path('candidate/<int:pk>', views.each_candidate, name="Candidate_detail"),
    path('short-listed', views.short_listed_candidates, name="shortlisted"),
    path('advanced-search', views.advance_search, name='advance_filter'),
    path('advanced-result', views.advance_result, name='advance_result'),
    # path('bout/', TemplateView.as_view(template_name="about.html")),
    # path('about/', vGreetingView.as_view(greeting="G'day")),
    # path('search/', SearchResultsListView.as_view(), name='search_results'),
]

