# Generated by Django 2.2.13 on 2020-06-17 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0002_load_initial_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="customtext",
            name="jgkjggh",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="customtext_jgkjggh",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
