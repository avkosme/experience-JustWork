# Generated by Django 2.1 on 2018-09-07 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Время добавления', verbose_name='Время добавления')),
                ('title', models.CharField(help_text='Заголовок аудио', max_length=150, verbose_name='Заголовок аудио')),
                ('url_file', models.CharField(help_text='Ссылка на файл', max_length=250, verbose_name='Ссылка на файл')),
                ('counter', models.BigIntegerField(default=0, help_text='Счетчик просмотров', verbose_name='Счетчик просмотров')),
                ('bit_rate', models.DecimalField(decimal_places=2, default=False, help_text='(бит в секунду)', max_digits=10, verbose_name='Битрейт')),
                ('page', models.ForeignKey(help_text='Страницы', on_delete=django.db.models.deletion.CASCADE, to='page.Page', verbose_name='Страницы')),
            ],
            options={
                'verbose_name': 'Аудио контент',
                'verbose_name_plural': 'Аудио контент',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Время добавления', verbose_name='Время добавления')),
                ('title', models.CharField(help_text='Заголовок текста', max_length=150, verbose_name='Заголовок текста')),
                ('counter', models.BigIntegerField(default=0, help_text='Счетчик просмотров', verbose_name='Счетчик просмотров')),
                ('page', models.ForeignKey(help_text='Страницы', on_delete=django.db.models.deletion.CASCADE, to='page.Page', verbose_name='Страницы')),
            ],
            options={
                'verbose_name': 'Аудио контент',
                'verbose_name_plural': 'Аудио контент',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Время добавления', verbose_name='Время добавления')),
                ('title', models.CharField(help_text='Заголовок видео', max_length=150, verbose_name='Заголовок видео')),
                ('url_file', models.CharField(help_text='Ссылка на файл', max_length=250, verbose_name='Ссылка на файл')),
                ('url_sub', models.CharField(help_text='Ссылка файл субтитров', max_length=250, verbose_name='Ссылка файл субтитров')),
                ('counter', models.BigIntegerField(default=0, help_text='Счетчик просмотров', verbose_name='Счетчик просмотров')),
                ('page', models.ForeignKey(help_text='Страницы', on_delete=django.db.models.deletion.CASCADE, to='page.Page', verbose_name='Страницы')),
            ],
            options={
                'verbose_name': 'Видео контент',
                'verbose_name_plural': 'Видео контент',
            },
        ),
    ]
