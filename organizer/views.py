from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView)

from core.utils import UpdateView
from user.decorators import (
    class_login_required,
    require_authenticated_permission)

from .forms import (
    NewsLinkForm, StartupForm, TagForm)
from .models import NewsLink, Startup, Tag
from .utils import (
    NewsLinkGetObjectMixin, PageLinksMixin,
    StartupContextMixin)


@require_authenticated_permission(
    'organizer.add_newslink')
class NewsLinkCreate(
        NewsLinkGetObjectMixin,
        StartupContextMixin,
        CreateView):
    form_class = NewsLinkForm
    model = NewsLink

    def get_initial(self):
        startup_slug = self.kwargs.get(
            self.startup_slug_url_kwarg)
        self.startup = get_object_or_404(
            Startup, slug__iexact=startup_slug)
        initial = {
            self.startup_context_object_name:
                self.startup,
        }
        initial.update(self.initial)
        return initial


@require_authenticated_permission(
    'organizer.delete_newslink')
class NewsLinkDelete(
        NewsLinkGetObjectMixin,
        StartupContextMixin,
        DeleteView):
    model = NewsLink
    slug_url_kwarg = 'newslink_slug'

    def get_success_url(self):
        return (self.object.startup
                .get_absolute_url())


@require_authenticated_permission(
    'organizer.change_newslink')
class NewsLinkUpdate(
        NewsLinkGetObjectMixin,
        StartupContextMixin,
        UpdateView):
    form_class = NewsLinkForm
    model = NewsLink
    slug_url_kwarg = 'newslink_slug'


@require_authenticated_permission(
    'organizer.add_startup')
class StartupCreate(CreateView):
    form_class = StartupForm
    model = Startup


@require_authenticated_permission(
    'organizer.delete_startup')
class StartupDelete(DeleteView):
    model = Startup
    success_url = reverse_lazy(
        'organizer_startup_list')


class StartupDetail(DetailView):
    model = Startup


class StartupList(PageLinksMixin, ListView):
    model = Startup
    paginate_by = 5  # 5 items per page


@require_authenticated_permission(
    'organizer.change_startup')
class StartupUpdate(UpdateView):
    form_class = StartupForm
    model = Startup


@require_authenticated_permission(
    'organizer.add_tag')
class TagCreate(CreateView):
    form_class = TagForm
    model = Tag


@require_authenticated_permission(
    'organizer.delete_tag')
class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy(
        'organizer_tag_list')


class TagDetail(DetailView):
    model = Tag


class TagList(PageLinksMixin, ListView):
    paginate_by = 5
    model = Tag


@require_authenticated_permission(
    'organizer.change_tag')
class TagUpdate(UpdateView):
    form_class = TagForm
    model = Tag
