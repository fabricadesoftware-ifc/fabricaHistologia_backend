# Generated by Django 4.2.13 on 2024-10-25 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_point_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='analyzed_functions',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='point',
            name='analyzed_structures',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='point',
            name='color',
            field=models.CharField(choices=[('yellow', 'Yellow'), ('blue', 'Blue'), ('red', 'Red')], max_length=6),
        ),
        migrations.AlterField(
            model_name='point',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
