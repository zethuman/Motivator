# Generated by Django 3.1.6 on 2021-04-18 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses_module', '0007_remove_content_is_watched'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificateforcourse',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]