# Generated by Django 2.2.3 on 2019-08-18 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0018_auto_20190818_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='board.Board'),
        ),
        migrations.AlterField(
            model_name='like',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Board'),
        ),
    ]
