from django.contrib import admin
from .models import Photo, Comment


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','author','created','updated']
    raw_id_fields = ['author']
    list_filter = ['created','updated','author']
    search_fields = ['text','created']
    ordering = ['-updated','-created']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','comment_author','created_date']
    raw_id_fields = ['comment_author']
    list_filter = ['created_date','comment_author']
    search_fields = ['comment_text','created_date']
    ordering = ['-created_date']


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Comment, CommentAdmin)
