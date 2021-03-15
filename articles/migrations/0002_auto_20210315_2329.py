# Generated by Django 3.1.3 on 2021-03-15 17:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='author', max_length=50),
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.CharField(default='content', max_length=1000),
        ),
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='fffff'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='title', max_length=200),
        ),
    ]
