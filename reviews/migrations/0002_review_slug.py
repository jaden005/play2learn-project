# Generated by Django 5.1.4 on 2025-01-10 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
    ]
