# Generated by Django 3.1.6 on 2021-03-29 12:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_module', '0004_auto_20210329_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmotivator',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='bookmotivator',
            name='deadline',
            field=models.DateTimeField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
