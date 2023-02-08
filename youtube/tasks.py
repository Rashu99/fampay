import datetime

import requests
import json

from .constants import YOUTUBE_API_URL
from .models import Video
from .utils import get_date_time_n_secs_ago
from fampay import celery_app


@celery_app.task
def fetch_videos():
    print("Running fetch video task ", datetime.datetime.now())

    # make API call to retrieve the latest videos
    published_after = get_date_time_n_secs_ago(1800)
    print("publishAfterTime", published_after)
    response = requests.get(YOUTUBE_API_URL, params={
        'part': 'snippet',
        'maxResults': 25,
        'q': 'music',
        'key': 'AIzaSyBodjcjdKbrqa2h4_lLe3F956n4BT9QmE4',
        'publishedAfter': published_after
    })
    data = json.loads(response.text)
    print("After Hitting Api Data is ")
    print(data)
    videos = data.get('items', [])

    # save videos in the database
    for video in videos:
        Video.objects.create(
            title=video['snippet']['title'],
            description=video['snippet']['description'],
            publish_datetime=video['snippet']['publishedAt'],
            video_id=video['id']['videoId'],
            channel_id=video['snippet']['channelId'],
            thumbnail_url=video['snippet']['thumbnails']['default']['url']
        )
