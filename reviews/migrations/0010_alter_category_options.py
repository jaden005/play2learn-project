# Generated by Django 5.1.4 on 2025-01-16 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_category_remove_review_tags_review_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
