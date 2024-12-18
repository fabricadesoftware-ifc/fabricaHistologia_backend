# Generated by Django 4.2.13 on 2024-09-13 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('position', models.JSONField()),
                ('color', models.CharField(max_length=255)),
                ('analyzed_structures', models.CharField(max_length=255)),
                ('analyzed_functions', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_analysis', models.DateField()),
                ('post_date', models.DateField()),
                ('type_cut', models.CharField(max_length=255)),
                ('increase', models.CharField(max_length=255)),
                ('coloring', models.CharField(max_length=255)),
                ('type_post', models.IntegerField(choices=[(1, 'Histologia'), (2, 'Patologia')], default=1)),
                ('verification_token', models.CharField(blank=True, max_length=100, null=True)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
    ]
