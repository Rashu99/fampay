import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fampay.settings')

app = Celery('fampay')

# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'fetch_youtube_videos': {
        'task': 'youtube.tasks.fetch_videos',
        'schedule': 30.0  # It will run every 30 seconds
    }
}
