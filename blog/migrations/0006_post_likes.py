# Generated by Django 4.2.15 on 2024-09-17 12:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0005_post_featured_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="liked_posts", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
