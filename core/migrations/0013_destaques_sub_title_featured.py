# Generated by Django 3.2.6 on 2021-08-16 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210814_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='destaques',
            name='sub_title_featured',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
