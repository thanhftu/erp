from django.urls import path

from ..views import (
    StartupCreate, StartupDelete, StartupUpdate,
    StartupDetail, StartupList)

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
    path('<slug>/delete/',
        StartupDelete.as_view(),
        name='organizer_startup_delete'),
    path('<slug>/update/',
        StartupUpdate.as_view(),
        name='organizer_startup_update'),
]
