from django.urls import path

from ..views import (
    NewsLinkCreate, NewsLinkDelete,
    NewsLinkUpdate, StartupCreate, StartupDelete,
    StartupDetail, StartupList, StartupUpdate)

urlpatterns = [
    path('',
        StartupList.as_view(),
        name='organizer_startup_list'),
    path('create/',
        StartupCreate.as_view(),
        name='organizer_startup_create'),
    path('<slug>/',
        StartupDetail.as_view(),
        name='organizer_startup_detail'),
    path('<startup_slug>/add_article_link/',
        NewsLinkCreate.as_view(),
        name='organizer_newslink_create'),
    path('<slug>/delete/',
        StartupDelete.as_view(),
        name='organizer_startup_delete'),
    path('<slug>/update/',
        StartupUpdate.as_view(),
        name='organizer_startup_update'),
    path('<startup_slug>/<newslink_slug>/delete/',
        NewsLinkDelete.as_view(),
        name='organizer_newslink_delete'),
    path('<startup_slug><newslink_slug>update/',
        NewsLinkUpdate.as_view(),
        name='organizer_newslink_update'),
]
