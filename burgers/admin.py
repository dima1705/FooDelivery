from django.contrib import admin
from .models import Burger


@admin.register(Burger)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    fields = ('name', 'description', 'price', 'image')
    search_fields = ('name', 'price')

