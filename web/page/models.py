from django.db import models
from django.template.defaultfilters import slugify
from unidecode import unidecode


class Page(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время добавления',
        help_text='Время добавления',
    )
    title = models.CharField(
        verbose_name='Название страницы',
        help_text='Название страницы',
        blank=False,
        max_length=150,
    )
    slug = models.CharField(
        verbose_name='Url страницы',
        help_text='Url страницы',
        blank=True,
        max_length=250,
    )
    status = models.BooleanField(
        verbose_name='Статус',
        help_text='Статус активна/скрыта',
        default=False,
    )

    def __str__(self):
        return ''.join((str(self.title)))

    def save(self, *args, **kwargs):
        if self.slug is not '/' and self.slug is '':
            self.slug = slugify(unidecode(self.title))
        super(Page, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Страницы'
        verbose_name_plural = 'Страницы'
