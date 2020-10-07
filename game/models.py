from django.db import models
from django_random_queryset import RandomManager

class PuzzleImage(models.Model):
    image = models.ImageField('Картинка', upload_to='puzzleimage/', blank=False, null=True)

    objects = RandomManager()

    def __str__(self):
        return f'Картинка пазла {self.id}'

    class Meta:
        verbose_name = "Картинка пазла"
        verbose_name_plural = "Картинки для пазлов"


class PuzzleVideo(models.Model):
    video = models.FileField('Видео', upload_to='puzzlevideo/', blank=False, null=True)

    objects = RandomManager()

    def __str__(self):
        return f'Видео пазла {self.id}'

    class Meta:
        verbose_name = "Видео пазла"
        verbose_name_plural = "Видео для пазлов"