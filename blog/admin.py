from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Comment, Post

# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status']
    summernote_fields = ('body', 'excerpt',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['author', 'body']