from rest_framework import serializers
from corp.models import IndustryCategory, Industry, IndustrySubcategory, IndustryDetail, Company, Contact, Note, Tag, OriginIndustryCategory, OriginIndustry

class IndustryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryCategory
        fields = '__all__'

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'

class IndustrySubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustrySubcategory
        fields = '__all__'

class IndustryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryDetail
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class OriginIndustryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OriginIndustryCategory
        fields = '__all__'

class OriginIndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OriginIndustry
        fields = '__all__'