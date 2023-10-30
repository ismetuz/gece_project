from django.contrib import admin
from .models import Category, Products, SliderItem, ContactInfo
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug','photo')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'slug', 'display_categories') 
    def display_categories(self, obj):
        return ", ".join([category.title for category in obj.category.all()])

    display_categories.short_description = 'Categories'


class SliderItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','image')

class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Products,ProductAdmin)
admin.site.register(SliderItem,SliderItemAdmin)
admin.site.register(ContactInfo,ContactInfoAdmin)
# Register your models here.
