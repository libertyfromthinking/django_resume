# Generated by Django 2.2.3 on 2019-07-11 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create Date'),
        ),
        migrations.AddField(
            model_name='board',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Modify Date'),
        ),
        migrations.AddField(
            model_name='board',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, help_text='자동으로 기입되니 입력하지 않으셔도 됩니다.', null=True, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
    ]
