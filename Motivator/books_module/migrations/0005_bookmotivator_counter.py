# Generated by Django 3.1.6 on 2021-04-20 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_module', '0004_auto_20210420_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmotivator',
            name='counter',
            field=models.IntegerField(default=0, verbose_name='Counter'),
        ),
    ]
