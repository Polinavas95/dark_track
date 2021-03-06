# Generated by Django 3.2.9 on 2021-11-20 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aggregator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(choices=[('plant', 'planting'), ('water', 'watering'), ('plant&water', 'planting&watering')], max_length=20)),
                ('name', models.CharField(default='unnamed', max_length=100)),
                ('width', models.FloatField()),
                ('aisle', models.FloatField(default=0.7)),
                ('row_width', models.FloatField(default=0.0)),
                ('num_of_sections', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessingArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortdesc', models.CharField(max_length=25)),
                ('shp', models.FileField(upload_to='geo/processing/')),
                ('shx', models.FileField(upload_to='geo/processing/')),
                ('dbf', models.FileField(upload_to='geo/processing/')),
                ('json', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortdesc', models.CharField(max_length=25)),
                ('shp', models.FileField(upload_to='geo/routing/')),
                ('shx', models.FileField(upload_to='geo/routing/')),
                ('dbf', models.FileField(upload_to='geo/routing/')),
                ('json', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TractorTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processing_area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='processing', to='track.processingarea')),
                ('routes', models.ManyToManyField(blank=True, related_name='routing', to='track.Route')),
            ],
        ),
        migrations.CreateModel(
            name='Tractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='??????-1221', max_length=100)),
                ('length', models.FloatField(default=4.95)),
                ('width', models.FloatField(default=2.25)),
                ('wheels_base', models.FloatField(default=2.45)),
                ('turning_radius', models.FloatField(default=5)),
                ('available_aggregators', models.ManyToManyField(blank=True, related_name='compability', to='track.Aggregator')),
            ],
        ),
    ]
