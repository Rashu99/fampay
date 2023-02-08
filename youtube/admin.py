from django.contrib import admin

from . import models


@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Video._meta.fields]
    search_fields = ('video_id', 'channel_id', 'title', 'description')
    list_filter = ('publish_datetime',)
