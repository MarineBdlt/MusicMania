# Generated by Django 4.0 on 2022-01-22 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_band_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='image',
        ),
    ]
