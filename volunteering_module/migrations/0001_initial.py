# Generated by Django 3.1.6 on 2021-04-12 11:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import volunteering_module.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerMotivator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('start', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='When did it start?')),
                ('end', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='When did it end?')),
                ('user', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='volunteers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Volunteering',
                'verbose_name_plural': 'Volunteering',
            },
            managers=[
                ('objects', volunteering_module.models.VolunteerMotivatorManager()),
            ],
        ),
        migrations.CreateModel(
            name='CertificateForVolunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True, verbose_name='Title')),
                ('number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Certificate number')),
                ('file', models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'jpg', 'png', 'jpeg'])])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('volunteer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='volunteers_certificates', to='volunteering_module.volunteermotivator')),
            ],
            options={
                'verbose_name': 'Volunteering certificate',
                'verbose_name_plural': 'Volunteering certificates',
            },
        ),
    ]
