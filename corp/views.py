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

def top(request):
    return render(request, 'corp/top.html', {})

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

# 企業を保存するたびにインデックスを更新するシグナルを設定します。
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.shortcuts import get_object_or_404
from .documents import CompanyDocument

def index_company(company_id):
    company = get_object_or_404(Company, id=company_id)
    company_document = CompanyDocument(
        meta={'id': company.id},
        name=company.name,
        description=company.description,
        industry=company.industry.name
    )
    company_document.save()

@receiver(post_save, sender=Company)
def index_company_on_save(sender, instance, **kwargs):
    index_company(instance.id)
