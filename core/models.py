from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from stdimage import StdImageField

class Post(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.TextField()
    slug = models.SlugField(max_length=255)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    image = StdImageField('Imagem', upload_to='img')
    body = RichTextField()
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Categories(models.Model):
    name = models.CharField(max_length=255)
    create = models.DateField(auto_now_add=True)
    update_cat = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name
    
    
  