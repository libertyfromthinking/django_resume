# Generated by Django 2.2.3 on 2019-08-13 02:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0010_auto_20190811_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Board'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
                ('Board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='board.Board')),
            ],
        ),
    ]