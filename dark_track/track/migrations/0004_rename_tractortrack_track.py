# Generated by Django 3.2.9 on 2021-11-20 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0003_tractortrack_shortdesc'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TractorTrack',
            new_name='Track',
        ),
    ]
