from django.urls import path, include
from . import views
from rest_framework import routers
from .views import CompanyViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)

urlpatterns = [
    path('company', views.company_list, name='company_list'),
    path('api/', include(router.urls)),
    path('email/', views.email_view, name='email_view'),
]
