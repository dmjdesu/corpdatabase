from django.contrib import admin
from .models import IndustryCategory, Industry, Company, Contact, Note, Tag

@admin.register(IndustryCategory)
class IndustryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',  'established_date', 'employees', 'revenue')
    list_filter = ('established_date',)
    search_fields = ('name', 'industry__name', 'description', 'address', 'city', 'state', 'country')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company', 'position')
    list_filter = ('company',)
    search_fields = ('first_name', 'last_name', 'company__name', 'position')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('company', 'content', 'created_at', 'updated_at')
    list_filter = ('company', 'created_at')
    search_fields = ('company__name', 'content')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
