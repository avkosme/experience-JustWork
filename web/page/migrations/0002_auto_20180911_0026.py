# Generated by Django 2.1 on 2018-09-11 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.CharField(blank=True, help_text='Url страницы', max_length=250, unique=True, verbose_name='Url страницы'),
        ),
    ]
