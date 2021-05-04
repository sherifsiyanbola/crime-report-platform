from django.shortcuts import render, get_list_or_404, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import TemplateView, CreateView, ListView
from .models import IssueCrime


class HomePageView(TemplateView):
    template_name = "board.html"
    
class CrimeCreateView(CreateView):
    model = IssueCrime
    template_name = 'report_crime.html'
    fields = ('crime_title', 'crime_description', 'crime_location', 'lga', 'street_address', 'date', 'phone_number' )
    
    success_url = reverse_lazy('home')
    
class SearchResultsView(ListView):
    model = IssueCrime
    template_name = 'search_results.html'
    
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = IssueCrime.objects.filter(
            Q(phone_number__icontains=query)
        )
        return object_list
    
# Create your views here.
