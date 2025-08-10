from django.contrib import admin
from .models import Category, Region, News

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author', 'id')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(News, NewsAdmin)