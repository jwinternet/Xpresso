# Generated by Django 4.2.10 on 2024-02-25 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horror_show', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='post',
            name='horror_show_publish_888b09_idx',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
    ]
