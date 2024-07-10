

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fabrica_histologia', '0002_organ_system_image_system_slidemicroscopypost_points_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='slidemicroscopypost',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fabrica_histologia.species'),
        ),
    ]
