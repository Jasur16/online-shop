from django.contrib import admin
from .models import ProductModel, ProductTagModel, CategoryModel, SizeTagModel, BrandTagModel, ColorTagModel


@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(SizeTagModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(BrandTagModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(ColorTagModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['code']
    list_display_links = ['code']
    search_fields = ['code']


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_at']
    list_display_links = ['title', 'price', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'price']
    autocomplete_fields = ['category', 'tags', 'sizes', 'colors']