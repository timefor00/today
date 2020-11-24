from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category','price','stock','available_display','available_order','created','updated']
    list_filter = ['available_display','created','updated','category']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price','stock','available_display','available_order']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id','author','studio','created','updated']
    raw_id_fields = ['author','studio']
    list_filter = ['created','updated','author','studio']
    search_fields = ['text','created']
    ordering = ['-updated','-created']


admin.site.register(Review, ReviewAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
