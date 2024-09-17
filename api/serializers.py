from rest_framework import serializers

from corp.models import *


class IndustryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryCategory
        fields = "__all__"


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = "__all__"


class IndustrySubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustrySubcategory
        fields = "__all__"


class IndustryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryDetail
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"


class OriginIndustryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OriginIndustryCategory
        fields = "__all__"


class OriginIndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OriginIndustry
        fields = "__all__"


class TagSmallcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TagSmallcategory
        fields = "__all__"


class TagSubcategorySerializer(serializers.ModelSerializer):
    smallcategories = TagSmallcategorySerializer(many=True, read_only=True)

    class Meta:
        model = TagSubcategory
        fields = "__all__"


class TagCategorySerializer(serializers.ModelSerializer):
    subcategories = TagSubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = TagCategory
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    prefecture_name = serializers.CharField(source="prefecture.name", read_only=True)

    class Meta:
        model = City
        fields = ["id", "code", "name", "name_kana", "prefecture_name"]


class PrefectureSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)

    class Meta:
        model = Prefecture
        fields = "__all__"
