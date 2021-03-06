# Generated by Django 3.1.6 on 2021-04-19 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('volunteering_module', '0003_auto_20210419_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificateforvolunteer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_volunteer_certificates', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='certificateforvolunteer',
            name='volunteer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='volunteers_certificates', to='volunteering_module.volunteermotivator'),
        ),
        migrations.AlterUniqueTogether(
            name='certificateforvolunteer',
            unique_together={('volunteer', 'user')},
        ),
    ]
