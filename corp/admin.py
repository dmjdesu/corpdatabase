from django.contrib import admin

from .models import (City, Company, Contact, Industry, IndustryCategory,
                     IndustryDetail, IndustrySubcategory, Note, OriginIndustry,
                     OriginIndustryCategory, Prefecture, TagCategory,
                     TagSmallcategory, TagSubcategory)


@admin.register(IndustryCategory)
class IndustryCategoryAdmin(admin.ModelAdmin):
    list_display = ("code", "name")
    search_fields = ("code", "name")


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "category")
    search_fields = ("code", "name")
    list_filter = ("category",)


@admin.register(IndustrySubcategory)
class IndustrySubcategoryAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "industry")
    search_fields = ("code", "name")
    list_filter = ("industry",)


@admin.register(IndustryDetail)
class IndustryDetailAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "subcategory")
    search_fields = ("code", "name")
    list_filter = ("subcategory",)


@admin.register(OriginIndustryCategory)
class OriginIndustryCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(OriginIndustry)
class OriginIndustryAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    search_fields = ("name",)
    list_filter = ("category",)


@admin.register(TagCategory)
class TagCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(TagSubcategory)
class TagSubcategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    search_fields = ("name",)
    list_filter = ("category",)


@admin.register(TagSmallcategory)
class TagSmallcategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "subcategory")
    search_fields = ("name",)
    list_filter = ("subcategory",)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "industry_detail",
        "origin_industry",
        "city",
        "state",
        "country",
    )
    search_fields = ("name", "city", "state", "country")
    list_filter = ("industry_detail", "origin_industry", "city", "state", "country")
    filter_horizontal = ("tags",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "company", "position")
    search_fields = ("first_name", "last_name", "company__name")
    list_filter = ("company",)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("company", "created_at", "updated_at")
    search_fields = ("company__name", "content")
    list_filter = ("created_at", "updated_at")


@admin.register(Prefecture)
class PrefectureAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "name_kana")
    search_fields = ("name", "name_kana")


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "name_kana", "prefecture")
    search_fields = ("name", "name_kana")
    list_filter = ("prefecture",)
