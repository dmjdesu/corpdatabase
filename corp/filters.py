from django_filters import rest_framework as filters

from .models import Company


class CompanyFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    industry_name = filters.CharFilter(
        field_name="industry__name", lookup_expr="icontains"
    )
    industry_category_name = filters.CharFilter(
        field_name="industry__category__name", lookup_expr="icontains"
    )
    city = filters.CharFilter(field_name="city", lookup_expr="icontains")
    country = filters.CharFilter(field_name="country", lookup_expr="icontains")

    class Meta:
        model = Company
        fields = ["name", "industry_name", "industry_category_name", "city", "country"]
