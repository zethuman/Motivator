# Generated by Django 3.1.6 on 2021-03-29 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books_module', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='essay',
            name='essays',
        ),
        migrations.AddField(
            model_name='essay',
            name='books',
            field=models.ForeignKey(default=3, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books_module.bookmotivator'),
        ),
    ]
