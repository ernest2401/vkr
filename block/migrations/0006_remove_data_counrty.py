# Generated by Django 2.2.24 on 2022-05-29 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0005_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='counrty',
        ),
    ]