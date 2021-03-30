# Generated by Django 3.1.6 on 2021-03-30 06:21

import datetime
from django.db import migrations, models
import books_module.models


class Migration(migrations.Migration):

    dependencies = [
        ('books_module', '0005_auto_20210329_1824'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='essay',
            managers=[
                ('objects', books_module.models.EssayMotivatorManager()),
            ],
        ),
        migrations.AlterField(
            model_name='bookmotivator',
            name='created',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='bookmotivator',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
