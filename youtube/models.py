from django.db import models
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    publish_datetime = models.DateTimeField()
    thumbnail_url = models.URLField()
    video_id = models.CharField(max_length=100, null=True)
    channel_id = models.CharField(max_length=100, null=True)
    search_vector = SearchVectorField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ', '.join(['title=' + self.title, 'description=' + self.description])

    class Meta:
        indexes = (GinIndex(fields=["search_vector"]),)
