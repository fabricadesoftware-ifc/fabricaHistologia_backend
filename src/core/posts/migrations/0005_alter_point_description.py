# Generated by Django 4.2.13 on 2024-10-22 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_point_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='description',
            field=models.TextField(),
        ),
    ]
