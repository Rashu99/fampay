# Generated by Django 4.1.6 on 2023-02-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0002_create_trigger'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='channel_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
