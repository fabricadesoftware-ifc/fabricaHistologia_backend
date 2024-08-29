# Generated by Django 4.2.13 on 2024-08-29 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_personaldata_user_user_personal_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='personal_data',
        ),
        migrations.AddField(
            model_name='personaldata',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
