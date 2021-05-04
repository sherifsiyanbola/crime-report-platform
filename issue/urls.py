from django.urls import path 
from .views import HomePageView, CrimeCreateView, SearchResultsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('report/', CrimeCreateView.as_view(), name = 'report'),
    path('search/', SearchResultsView.as_view(), name="search_results"),
]
