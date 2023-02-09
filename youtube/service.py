from youtube.models import Video


class YoutubeService:
    """
        This class contains business logic or computation if any
        required for youtube service
    """

    @classmethod
    def process_videos(cls, videos: list):
        """
            This function is responsible for saving video data to db
        """
        if not videos or len(videos) == 0:
            print("No videos fetched from youtube search api")
            return

        for video in videos:
            try:
                Video.objects.create(
                    title=video['snippet']['title'],
                    description=video['snippet']['description'],
                    publish_datetime=video['snippet']['publishedAt'],
                    video_id=video['id']['videoId'],
                    channel_id=video['snippet']['channelId'],
                    thumbnail_url=video['snippet']['thumbnails']['default']['url']
                )
            except Exception as e:
                print("Error while saving video to database", e)
