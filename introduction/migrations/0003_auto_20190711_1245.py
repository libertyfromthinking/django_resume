# Generated by Django 2.2.3 on 2019-07-11 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction', '0002_auto_20190707_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, help_text='빈칸으로 두면 자동으로 입력됩니다', null=True, unique=True, verbose_name='Slug'),
        ),
    ]
