# Generated by Django 3.1.6 on 2021-04-25 07:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteering_module', '0004_auto_20210419_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificateforvolunteer',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='certificates', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'jpg', 'png', 'jpeg'])]),
        ),
    ]