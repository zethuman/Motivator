# Generated by Django 3.1.6 on 2021-04-25 07:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_module', '0005_bookmotivator_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay',
            name='essay',
            field=models.FileField(blank=True, null=True, upload_to='essays', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'jpg', 'png', 'jpeg'])]),
        ),
    ]
