from django.urls import include, path
from rest_framework import routers

from . import views
from .views import CompanyViewSet

urlpatterns = [
    path("", views.top, name="top"),
    path("company/", views.company_list, name="company_list"),  # 末尾にスラッシュを追加
]
