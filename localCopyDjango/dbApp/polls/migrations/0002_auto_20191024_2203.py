# Generated by Django 3.1.dev20191024131625 on 2019-10-25 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hours',
            old_name='restuarant_name',
            new_name='restaurant_name',
        ),
    ]
