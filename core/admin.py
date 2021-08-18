from django.contrib import admin
from .models import Post, Categories, Banner, Destaques

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', ]
    list_display = ('title', 'sub_title', 'created', 'update')
    ordering = ['created']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    search_fields = ['title', ]
    list_display = ('title', 'sub_title_banner', 'created_banner', 'update_banner')
    ordering = ['created_banner']
    prepopulated_fields = {'slug_banner': ('title',)}

@admin.register(Destaques)
class DestaquesAdmin(admin.ModelAdmin):
    search_fields = ['title_featured', ]
    list_display = ('title_featured', 'slug_featured', 'created_featured', 'update_featured')
    ordering = ['created_featured']
    prepopulated_fields = {'slug_featured': ('title_featured',)}

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
    list_display = ('name', 'create', 'update_cat')  
    ordering = ['create', ]  