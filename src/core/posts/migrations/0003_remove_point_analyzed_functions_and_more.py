# Generated by Django 4.2.13 on 2024-10-22 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='analyzed_functions',
        ),
        migrations.RemoveField(
            model_name='point',
            name='analyzed_structures',
        ),
        migrations.AlterField(
            model_name='point',
            name='color',
            field=models.IntegerField(choices=[(1, 'yellow'), (2, 'red'), (3, 'blue')], default=1),
        ),
    ]