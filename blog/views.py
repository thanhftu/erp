from django.urls import reverse_lazy
from django.views.generic import (
    ArchiveIndexView, CreateView, DeleteView,
    DetailView, MonthArchiveView, YearArchiveView)

from core.utils import UpdateView
from user.decorators import \
    require_authenticated_permission

from .forms import PostForm
from .models import Post
from .utils import DateObjectMixin


class PostArchiveMonth(MonthArchiveView):
    model = Post
    date_field = 'pub_date'
    month_format = '%m'


class PostArchiveYear(YearArchiveView):
    model = Post
    date_field = 'pub_date'
    make_object_list = True


@require_authenticated_permission(
    'blog.add_post')
class PostCreate(CreateView):
    form_class = PostForm
    model = Post


@require_authenticated_permission(
    'blog.delete_post')
class PostDelete(DateObjectMixin, DeleteView):
    allow_future = True
    date_field = 'pub_date'
    model = Post
    success_url = reverse_lazy('blog_post_list')


class PostDetail(DateObjectMixin, DetailView):
    allow_future = True
    date_field = 'pub_date'
    model = Post


class PostList(ArchiveIndexView):
    allow_empty = True
    allow_future = True
    context_object_name = 'post_list'
    date_field = 'pub_date'
    make_object_list = True
    model = Post
    paginate_by = 5
    template_name = 'blog/post_list.html'


@require_authenticated_permission(
    'blog.change_post')
class PostUpdate(DateObjectMixin, UpdateView):
    allow_future = True
    date_field = 'pub_date'
    form_class = PostForm
    model = Post
