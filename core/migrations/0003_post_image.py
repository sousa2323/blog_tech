# Generated by Django 3.2.6 on 2021-08-10 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_post_sub_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to='imagens'),
            preserve_default=False,
        ),
    ]
