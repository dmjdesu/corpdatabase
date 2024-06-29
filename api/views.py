from rest_framework import viewsets
from corp.models import IndustryCategory, Industry, OriginIndustryCategory, OriginIndustry, IndustrySubcategory, IndustryDetail, Company, Contact, Note
from .serializers import *

class IndustryCategoryViewSet(viewsets.ModelViewSet):
    queryset = IndustryCategory.objects.all()
    serializer_class = IndustryCategorySerializer

class IndustryViewSet(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer

class IndustrySubcategoryViewSet(viewsets.ModelViewSet):
    queryset = IndustrySubcategory.objects.all()
    serializer_class = IndustrySubcategorySerializer

class IndustryDetailViewSet(viewsets.ModelViewSet):
    queryset = IndustryDetail.objects.all()
    serializer_class = IndustryDetailSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class OriginIndustryCategoryViewSet(viewsets.ModelViewSet):
    queryset = OriginIndustryCategory.objects.all()
    serializer_class = OriginIndustryCategorySerializer

class OriginIndustryViewSet(viewsets.ModelViewSet):
    queryset = OriginIndustry.objects.all()
    serializer_class = OriginIndustrySerializer

class OriginIndustryCategoryViewSet(viewsets.ModelViewSet):
    queryset = OriginIndustryCategory.objects.all()
    serializer_class = OriginIndustryCategorySerializer

class OriginIndustryViewSet(viewsets.ModelViewSet):
    queryset = OriginIndustry.objects.all()
    serializer_class = OriginIndustrySerializer

class TagCategoryViewSet(viewsets.ModelViewSet):
    queryset = TagCategory.objects.all()
    serializer_class = TagCategorySerializer

class TagSubcategoryCategoryViewSet(viewsets.ModelViewSet):
    queryset = TagSubcategory.objects.all()
    serializer_class = TagSubcategorySerializer

class TagSmallcategoryViewSet(viewsets.ModelViewSet):
    queryset = TagSmallcategory.objects.all()
    serializer_class = TagSmallcategorySerializer

class PrefectureViewSet(viewsets.ModelViewSet):
    queryset = Prefecture.objects.all()
    serializer_class = PrefectureSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer