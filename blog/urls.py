from django.urls import path

from .views import (PostArchiveYear,MonthArchiveView,
    PostCreate, PostDelete, PostList, PostUpdate,
    PostDetail)

urlpatterns = [
    path('',
        PostList.as_view(),
        name='blog_post_list'),
    path('create/',
        PostCreate.as_view(),
        name='blog_post_create'),
        path('<year>/<month>/',
                MonthArchiveView.as_view(),
                name='blog_post_archive_month'),
    path('<year>/',
            PostArchiveYear.as_view(),
            name='blog_post_archive_year'),
    path('<year>/<month>/<slug>/',
        PostDetail.as_view(),
        name='blog_post_detail'),
    path('<year>\d{4}/<month>\d{1,2}/<slug>/update/delete/',
        PostDelete.as_view(),
        name='blog_post_delete'),
    path('<year>\d{4}/<month>\d{1,2}/<slug>/update/',
        PostUpdate.as_view(),
        name='blog_post_update'),
]
