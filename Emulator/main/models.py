from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название жанра')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Game(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название игры')
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, verbose_name='Жанр')
    description = models.TextField(verbose_name='Описание игры')
    release_year = models.PositiveIntegerField(verbose_name='Год выхода')
    rom_file = models.FileField(
        upload_to='roms/', verbose_name='ROM файл')
    cover_image = models.ImageField(
        upload_to='covers/', verbose_name='Обложка игры')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
