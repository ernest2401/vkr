# Generated by Django 2.2.24 on 2022-05-28 12:55

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название запчасти')),
                ('content', models.TextField(blank=True, verbose_name='Описание')),
                ('url', models.SlugField(max_length=160)),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Стоимость')),
                ('publish', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')),
                ('image', models.ImageField(blank=True, null=True, upload_to='bboard/')),
            ],
            options={
                'verbose_name': 'Название запчасти',
                'verbose_name_plural': 'Название запчастей',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда',
                'verbose_name_plural': 'Звезды',
            },
        ),
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
                ('url', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрики',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=100, verbose_name='Текст')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='block.Reviews', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP')),
                ('product', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='block.Product', verbose_name='Запчасть')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='block.RatingStar', verbose_name='звезда')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='block.Rubric', verbose_name='Рубрика'),
        ),
    ]
