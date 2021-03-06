# Generated by Django 3.2.6 on 2021-08-14 21:23

import ckeditor.fields
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_banner_update_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destaques',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_featured', models.CharField(max_length=255)),
                ('slug_featured', models.SlugField(max_length=255)),
                ('image_featured', stdimage.models.StdImageField(upload_to='img_featured', verbose_name='ImageFeatured')),
                ('body_featured', ckeditor.fields.RichTextField()),
                ('created_featured', models.DateTimeField(auto_now_add=True)),
                ('update_featured', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
