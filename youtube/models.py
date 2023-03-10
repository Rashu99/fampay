import datetime

from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    publish_datetime = models.DateTimeField()
    thumbnail_url = models.URLField()
    video_id = models.CharField(max_length=150, unique=True)  # Later we can index on this
    channel_id = models.CharField(max_length=150)  # Later we can index on this
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ', '.join(['title=' + self.title, 'description=' + self.description])


class APIAuthKey(models.Model):
    auth_key = models.CharField(max_length=250, db_index=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    exhausted = models.BooleanField(default=False)

    @classmethod
    def get_auth_key(cls):
        """
            This function returns the non exhausted auth api key
            sorted by created time in ascending order
        """
        api_key = cls.objects.filter(exhausted=False).order_by('created').values()
        if len(api_key):
            return api_key[0]['auth_key']
        return None

    @classmethod
    def mark_auth_key_exhausted(cls, auth_key):
        """
            This function marks the api auth key as exhausted
        """
        row = cls.objects.get(auth_key=auth_key)
        row.exhausted = True
        row.updated = datetime.datetime.now()
        row.save()
        return row
