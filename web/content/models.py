from django.db import models
from page.models import Page


class Video(models.Model):
    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        verbose_name='Страницы',
        help_text='Страницы',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время добавления',
        help_text='Время добавления',
    )
    title = models.CharField(
        verbose_name='Заголовок видео',
        help_text='Заголовок видео',
        blank=False,
        max_length=150,
    )
    url_file = models.CharField(
        verbose_name='Ссылка на файл',
        help_text='Ссылка на файл',
        blank=False,
        max_length=250,
    )

    url_sub = models.CharField(
        verbose_name='Ссылка файл субтитров',
        help_text='Ссылка файл субтитров',
        blank=False,
        max_length=250,
    )
    counter = models.BigIntegerField(
        verbose_name='Счетчик просмотров',
        help_text='Счетчик просмотров',
        blank=False,
        default=0
    )

    def __str__(self):
        return ' '.join((str(self.title), str(self.url_file)))

    class Meta:
        verbose_name = 'Видео контент'
        verbose_name_plural = 'Видео контент'


class Audio(models.Model):
    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        verbose_name='Страницы',
        help_text='Страницы',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время добавления',
        help_text='Время добавления',
    )
    title = models.CharField(
        verbose_name='Заголовок аудио',
        help_text='Заголовок аудио',
        blank=False,
        max_length=150,
    )
    url_file = models.CharField(
        verbose_name='Ссылка на файл',
        help_text='Ссылка на файл',
        blank=False,
        max_length=250,
    )

    counter = models.BigIntegerField(
        verbose_name='Счетчик просмотров',
        help_text='Счетчик просмотров',
        blank=False,
        default=0
    )

    bit_rate = models.DecimalField(
        verbose_name='Битрейт',
        help_text='(бит в секунду)',
        max_digits=10,
        decimal_places=2,
        default=False,
        blank=False,
    )

    def __str__(self):
        return ' '.join((str(self.title), str(self.url_file)))

    class Meta:
        verbose_name = 'Аудио контент'
        verbose_name_plural = 'Аудио контент'


class Text(models.Model):
    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        verbose_name='Страницы',
        help_text='Страницы',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время добавления',
        help_text='Время добавления',
    )
    title = models.CharField(
        verbose_name='Заголовок текста',
        help_text='Заголовок текста',
        blank=False,
        max_length=150,
    )

    counter = models.BigIntegerField(
        verbose_name='Счетчик просмотров',
        help_text='Счетчик просмотров',
        blank=False,
        default=0
    )

    def __str__(self):
        return ' '.join((str(self.title)))

    class Meta:
        verbose_name = 'Аудио контент'
        verbose_name_plural = 'Аудио контент'
