# Generated by Django 4.1.6 on 2023-02-08 13:40

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('publish_datetime', models.DateTimeField()),
                ('thumbnail_url', models.URLField()),
                ('search_vector', django.contrib.postgres.search.SearchVectorField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='video',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='youtube_vid_search__985420_gin'),
        ),
    ]