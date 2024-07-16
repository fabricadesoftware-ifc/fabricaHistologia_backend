# Generated by Django 4.2.13 on 2024-07-16 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabrica_histologia', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slidemicroscopypost',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='slidemicroscopypost',
            name='name',
            field=models.CharField(default='sdsad', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slidemicroscopypost',
            name='verification_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
