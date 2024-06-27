from rest_framework import viewsets
from corp.models import IndustryCategory, Industry, IndustrySubcategory, IndustryDetail, Company, Contact, Note, Tag
from .serializers import (IndustryCategorySerializer, IndustrySerializer, IndustrySubcategorySerializer, IndustryDetailSerializer, CompanySerializer, ContactSerializer, NoteSerializer, TagSerializer)

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

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer