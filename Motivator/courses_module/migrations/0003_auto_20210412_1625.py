# Generated by Django 3.1.6 on 2021-04-12 10:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses_module', '0002_auto_20210412_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursemotivator',
            name='user',
        ),
        migrations.AddField(
            model_name='coursemotivator',
            name='user',
            field=models.ManyToManyField(related_name='courses', to=settings.AUTH_USER_MODEL),
        ),
    ]
