from rest_framework import generics
from .serializers import VideoSerializer
from rest_framework.pagination import PageNumberPagination
from django.contrib.postgres.search import SearchVector, SearchQuery
from .models import Video


class VideoPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_limit'

    def get_page_size(self, request):
        page_size = self.page_size
        if self.page_size_query_param:
            try:
                page_size = int(request.query_params[self.page_size_query_param])
                if page_size <= 0:
                    raise ValueError
            except (KeyError, ValueError):
                pass
        return page_size


class ListVideos(generics.ListAPIView):
    queryset = Video.objects.order_by('-publish_datetime').values('id', 'title', 'description', 'publish_datetime',
                                                                  'thumbnail_url', 'video_id', 'channel_id')
    serializer_class = VideoSerializer
    pagination_class = VideoPagination


class ListVideoSearch(generics.ListAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        search_text = self.request.query_params.get('query', None)
        vector = SearchVector('title', 'description', config='english')
        query = SearchQuery(search_text)
        query_set = Video.objects.annotate(search=vector).filter(search=query).values('id', 'title', 'description',
                                                                                      'publish_datetime',
                                                                                      'thumbnail_url', 'video_id',
                                                                                      'channel_id')
        return query_set
