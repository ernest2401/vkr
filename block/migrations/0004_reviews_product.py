# Generated by Django 2.2.24 on 2022-05-28 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0003_auto_20220528_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='product',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='block.Product', verbose_name='Запчасть'),
            preserve_default=False,
        ),
    ]
