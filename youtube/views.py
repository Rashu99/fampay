from django.contrib.postgres.search import SearchVector, SearchQuery
from rest_framework import generics, status
from .serializers import VideoSerializer, APIAuthKeySerializer
from rest_framework.pagination import PageNumberPagination
from .models import Video, APIAuthKey
from rest_framework.response import Response
from rest_framework import exceptions


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
    """
        This view is for getting all the videos with pagination
        We can pass the query param 'page_limit' to give page size
        otherwise
            It will take default page size as 10

        Refer VideoPagination class for pagination
    """
    queryset = Video.objects.order_by('-publish_datetime').values('id', 'title', 'description', 'publish_datetime',
                                                                  'thumbnail_url', 'video_id', 'channel_id')
    serializer_class = VideoSerializer
    pagination_class = VideoPagination

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ListVideoSearch(generics.ListAPIView):
    """
        This view is for getting the videos by search keyword.
        We can pass query param 'query' to search video. It will search in title and description of video

        Used search vector to optimise the search
    """
    serializer_class = VideoSerializer

    def get_queryset(self):
        search_text = self.request.query_params.get('query', None)
        if not search_text:
            raise exceptions.ValidationError({'error': 'Query parameter is missing'})
        vector = SearchVector('title', 'description', config='english')
        query = SearchQuery(search_text)

        query_set = Video.objects.annotate(search=vector).filter(search=query).values('id', 'title', 'description',
                                                                                      'publish_datetime',
                                                                                      'thumbnail_url', 'video_id',
                                                                                      'channel_id')
        return query_set

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except exceptions.ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AddAuthKey(generics.CreateAPIView):
    """
        This view is responsible for adding auth keys
    """
    serializer_class = APIAuthKeySerializer
    queryset = APIAuthKey.objects.all()

    def create(self, request, *args, **kwargs):
        auth_key = request.data.get('auth_key', None)
        if not auth_key:
            return Response({'error': 'Auth key is missing. Please provide auth_key in header'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            return super().create(request, *args, **kwargs)
        except exceptions.ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
