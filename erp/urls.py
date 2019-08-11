from django.urls import path, include
from django.contrib import admin

from blog import urls as blog_urls
from contact import urls as contact_urls
from organizer.urls import (
    newslink as newslink_urls,
    startup as startup_urls, tag as tag_urls)

from .views import redirect_root

urlpatterns = [
    path('', redirect_root),
    path('admin/', admin.site.urls),
    path('blog/', include(blog_urls)),
    path('contact/', include(contact_urls)),
    path('newslink/', include(newslink_urls)),
    path('startup/', include(startup_urls)),
    path('tag/', include(tag_urls)),
]
