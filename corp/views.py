# your_app_name/views.py
from django.shortcuts import render
from .models import Company
from .forms import CompanySearchForm
from django.db.models import Q

def company_list(request):
    form = CompanySearchForm(request.GET)
    companies = Company.objects.all()
    
    if form.is_valid():
        name = form.cleaned_data.get('name')
        industry_category = form.cleaned_data.get('industry_category')
        industry = form.cleaned_data.get('industry')
        city = form.cleaned_data.get('city')
        country = form.cleaned_data.get('country')

        if name:
            companies = companies.filter(name__icontains=name)
        if industry_category:
            companies = companies.filter(industry__category=industry_category)
        if industry:
            companies = companies.filter(industry=industry)
        if city:
            companies = companies.filter(city__icontains=city)
        if country:
            companies = companies.filter(country__icontains=country)
    
    return render(request, 'corp/company_list.html', {'companies': companies, 'form': form})

from rest_framework import viewsets
from .models import Company
from .serializers import CompanySerializer
from .filters import CompanyFilter
from django_filters.rest_framework import DjangoFilterBackend

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CompanyFilter
