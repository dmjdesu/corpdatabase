from django.urls import path, include
from rest_framework import routers
from .views import (IndustryCategoryViewSet, IndustryViewSet, OriginIndustryCategoryViewSet, OriginIndustryViewSet, IndustrySubcategoryViewSet, IndustryDetailViewSet, CompanyViewSet, ContactViewSet, NoteViewSet, TagViewSet)
from . import views

router = routers.DefaultRouter()
router.register(r'industry_categories', IndustryCategoryViewSet)
router.register(r'industries', IndustryViewSet)
router.register(r'industry_subcategories', IndustrySubcategoryViewSet)
router.register(r'industry_details', IndustryDetailViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'tags', TagViewSet)

router.register(r'origin_industry_categories', OriginIndustryCategoryViewSet)
router.register(r'origin_industries', OriginIndustryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
