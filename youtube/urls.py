from django.urls import path

from . import views

urlpatterns = [
    path('getVideos', views.ListVideos.as_view()),
    path('searchVideos', views.ListVideoSearch.as_view()),
]
