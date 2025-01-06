# Generated by Django 5.1.4 on 2025-01-06 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='cover_image',
            field=models.ImageField(upload_to='covers/', verbose_name='Обложка игры'),
        ),
        migrations.AlterField(
            model_name='game',
            name='rom_file',
            field=models.FileField(upload_to='roms/', verbose_name='ROM файл'),
        ),
    ]