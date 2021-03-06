# Generated by Django 3.1.6 on 2021-04-12 10:13

import courses_module.models
import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseMotivator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Deadline')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('rating', models.FloatField(default=0.0, verbose_name='Rating')),
                ('user', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('video', models.CharField(blank=True, default='', max_length=300, verbose_name='Videos')),
                ('is_watched', models.BooleanField(default=False, verbose_name='Is Watched?')),
                ('course', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='courses_content', to='courses_module.coursemotivator')),
                ('user', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='contents', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Contents',
            },
            managers=[
                ('objects', courses_module.models.ContentMotivatorManager()),
            ],
        ),
        migrations.CreateModel(
            name='CertificateForCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True, verbose_name='Title')),
                ('number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Certificate number')),
                ('file', models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'jpg', 'png', 'jpeg'])])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='courses_certificate', to='courses_module.coursemotivator')),
            ],
            options={
                'verbose_name': 'Course certificate',
                'verbose_name_plural': 'Course certificates',
            },
        ),
    ]
