from django.urls import path
from django.contrib.auth import \
    views as auth_views
from django.contrib.auth.forms import \
    AuthenticationForm
from django.views.generic import RedirectView

app_name = 'user'
urlpatterns = [
    path('',
        RedirectView.as_view(
            pattern_name='dj-auth:login',
            permanent=False)),
    path('login/',
        auth_views.LoginView.as_view(),
        # {'template_name': 'registration/login.html'},
        name='login'),
    path('logout/',
        auth_views.LogoutView.as_view(),
        {'template_name': 'registration/logged_out.html',
         'extra_context':
             {'form': AuthenticationForm}},
        name='logout'),
]
