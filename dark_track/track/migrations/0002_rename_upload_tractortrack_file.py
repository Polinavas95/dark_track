# Generated by Django 3.2.9 on 2021-11-19 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tractortrack',
            old_name='upload',
            new_name='file',
        ),
    ]
