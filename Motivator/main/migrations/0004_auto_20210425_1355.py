# Generated by Django 3.1.6 on 2021-04-25 07:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_profile_certificates_for_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc'])]),
        ),
    ]
