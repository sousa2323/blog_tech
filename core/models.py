from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from stdimage import StdImageField

class Post(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.TextField(max_length=151)
    slug = models.SlugField(max_length=255)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    image = StdImageField('Imagem', upload_to='img')
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

class Banner(models.Model):
    title = models.CharField(max_length=255)
    sub_title_banner = models.TextField(max_length=151)
    slug_banner = models.SlugField(max_length=255)
    image_banner = StdImageField('ImagemBanner', upload_to='img_banner')
    body_banner = RichTextField()
    created_banner = models.DateTimeField(auto_now_add=True)
    update_banner = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Destaques(models.Model):
    title_featured = models.CharField(max_length=255)
    slug_featured = models.SlugField(max_length=255)
    image_featured = StdImageField('ImageFeatured', upload_to='img_featured')
    body_featured = RichTextField()
    created_featured = models.DateTimeField(auto_now_add=True)
    update_featured = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_featured
    

class Categories(models.Model):
    name = models.CharField(max_length=255)
    create = models.DateTimeField(auto_now_add=True)
    update_cat = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name
    
    
  