from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['cat_name']


@admin.register(News)
class AdminNews(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'slug')
    list_display = ['cat_id', 'title', 'slug', 'image', 'description']


@admin.register(CompanySettings)
class AdminComanySettings(admin.ModelAdmin):
    list_display = ['c_name', 'c_email', 'c_address', 'c_phone', 'c_logo']


@admin.register(Contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ['email', 'subject', 'message']
