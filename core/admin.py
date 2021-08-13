from django.contrib import admin
from .models import Post, Categories

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sub_title', 'created', 'update')
    ordering = ['created']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'create', 'update_cat')    