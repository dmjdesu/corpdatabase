from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r"industry_categories", IndustryCategoryViewSet)
router.register(r"industries", IndustryViewSet)
router.register(r"industry_subcategories", IndustrySubcategoryViewSet)
router.register(r"industry_details", IndustryDetailViewSet)
router.register(r"companies", CompanyViewSet)
router.register(r"contacts", ContactViewSet)
router.register(r"notes", NoteViewSet)

router.register(r"origin_industry_categories", OriginIndustryCategoryViewSet)
router.register(r"origin_industries", OriginIndustryViewSet)

router.register(r"tags_categories", TagCategoryViewSet)
router.register(r"tags_subcategories", TagSubcategoryCategoryViewSet)
router.register(r"tags_smallcategories", TagSmallcategoryViewSet)

router.register(r"prefectures", PrefectureViewSet)
router.register(r"cities", CityViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
