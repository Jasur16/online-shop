from django.contrib import admin
from .models import ContactModel, CaruselModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_display_links = ['name', 'email']
    search_fields = ['name', 'email', 'message']
    list_filter = ['created_at']


@admin.register(CaruselModel)
class CaruselModelAdmin(admin.ModelAdmin):
    list_display = ['carusel_text', 'carusel_title']
    list_display_links = ['carusel_text', 'carusel_title']
    search_fields = ['carusel_title']