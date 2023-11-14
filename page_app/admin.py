from django.contrib import admin
from .models import Category, Products, SliderItem, ContactInfo, MainAdvert
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from .resource import ProductResource, CategoryResource

@admin.register(SliderItem)
class SliderItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','image')
@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Products)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource

@admin.register(MainAdvert)
class MainAdvertAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','image')
