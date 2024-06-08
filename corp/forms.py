# your_app_name/forms.py

from django import forms
from .models import Industry, IndustryCategory

class CompanySearchForm(forms.Form):
    name = forms.CharField(label='企業名', required=False)
    industry_category = forms.ModelChoiceField(
        queryset=IndustryCategory.objects.all(), label='業界大分類', required=False
    )
    industry = forms.ModelChoiceField(
        queryset=Industry.objects.all(), label='業界中分類', required=False
    )
    city = forms.CharField(label='市区町村', required=False)
    country = forms.CharField(label='国', required=False)

class EmailForm(forms.Form):
    email = forms.EmailField(label='Your email')

