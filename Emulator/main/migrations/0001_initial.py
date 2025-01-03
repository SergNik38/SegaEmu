# Generated by Django 5.1.4 on 2025-01-03 04:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название жанра')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название игры')),
                ('description', models.TextField(verbose_name='Описание игры')),
                ('release_year', models.PositiveIntegerField(verbose_name='Год выхода')),
                ('rom_file', models.FileField(upload_to='media/roms/', verbose_name='ROM файл')),
                ('cover_image', models.ImageField(upload_to='media/covers/', verbose_name='Обложка игры')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
            },
        ),
    ]